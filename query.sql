-- STEP 1: pool benchmark = selected employees (runtime input)
WITH benchmark_pool AS (
    SELECT *
    FROM employees_performers
    WHERE employee_id = ANY(:benchmark_ids)  -- << PARAMETERIZED
),

-- STEP 2: baseline (median) per TV per role/position
baseline AS (
    SELECT DISTINCT
        bp.position,
        t.tv_name,
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY t.tv_value) AS baseline_score
    FROM benchmark_pool bp
    CROSS JOIN LATERAL (
        VALUES
            ('pillar_gdr', bp.pillar_gdr),
            ('pillar_cex', bp.pillar_cex),
            ('pillar_ids', bp.pillar_ids),
            ('pillar_qdd', bp.pillar_qdd),
            ('pillar_sto', bp.pillar_sto),
            ('pillar_sea', bp.pillar_sea),
            ('pillar_vcu', bp.pillar_vcu),
            ('pillar_lie', bp.pillar_lie),
            ('pillar_ftc', bp.pillar_ftc),
            ('pillar_csi', bp.pillar_csi),
            ('pauli', bp.pauli),
            ('faxtor', bp.faxtor),
            ('iq', bp.iq),
            ('gtq', bp.gtq),
            ('disc_id', bp.disc_id),
            ('mbti_id', bp.mbti_id),
            ('years_of_service_months', bp.years_of_service_months),
            ('grade', bp.grade),
            ('education_id', bp.education_id)
    ) AS t(tv_name, tv_value)
    GROUP BY bp.position, t.tv_name
),

-- STEP 3: long table kandidat + baseline
candidate_values AS (
    SELECT DISTINCT
        e.employee_id,
        e.position,
        e.grade,
        e.education_id,
        d.name AS directorate,
        b.tv_name,
        b.baseline_score,
        CASE b.tv_name
            WHEN 'pillar_gdr' THEN e.pillar_gdr
            WHEN 'pillar_cex' THEN e.pillar_cex
            WHEN 'pillar_ids' THEN e.pillar_ids
            WHEN 'pillar_qdd' THEN e.pillar_qdd
            WHEN 'pillar_sto' THEN e.pillar_sto
            WHEN 'pillar_sea' THEN e.pillar_sea
            WHEN 'pillar_vcu' THEN e.pillar_vcu
            WHEN 'pillar_lie' THEN e.pillar_lie
            WHEN 'pillar_ftc' THEN e.pillar_ftc
            WHEN 'pillar_csi' THEN e.pillar_csi
            WHEN 'pauli' THEN e.pauli
            WHEN 'faxtor' THEN e.faxtor
            WHEN 'iq' THEN e.iq
            WHEN 'gtq' THEN e.gtq
            WHEN 'disc_id' THEN e.disc_id
            WHEN 'mbti_id' THEN e.mbti_id
            WHEN 'years_of_service_months' THEN e.years_of_service_months
            WHEN 'grade' THEN e.grade
            WHEN 'education_id' THEN e.education_id
        END::numeric AS user_score
    FROM employees_performers e
    JOIN baseline b USING (position)
    LEFT JOIN employees emp USING (employee_id)
    LEFT JOIN dim_directorates d USING (directorate_id)
),

-- STEP 4: match per TV
tv_match AS (
    SELECT *,
        (user_score / NULLIF(baseline_score, 0)) * 100 AS tv_match_rate,
        CASE
            WHEN tv_name LIKE 'pillar_%' THEN 'Competency'
            WHEN tv_name IN ('pauli','faxtor','iq','gtq','disc_id','mbti_id') THEN 'Psychometric'
            WHEN tv_name LIKE 'theme_%' THEN 'Strength'
            ELSE 'Context'
        END AS tgv_name
    FROM candidate_values
),

-- STEP 5: TGV Aggregation
tgv_agg AS (
    SELECT
        employee_id,
        tgv_name,
        AVG(tv_match_rate) AS tgv_match_rate
    FROM tv_match
    GROUP BY employee_id, tgv_name
),

-- STEP 6: Final Weighted Score
final_agg AS (
    SELECT
        employee_id,
        SUM(
            CASE tgv_name
                WHEN 'Competency'  THEN tgv_match_rate * 0.282
                WHEN 'Psychometric' THEN tgv_match_rate * 0.134
                WHEN 'Strength'    THEN tgv_match_rate * 0.551
                WHEN 'Context'     THEN tgv_match_rate * 0.032
            END
        ) AS final_match_rate
    FROM tgv_agg
    GROUP BY employee_id
)

SELECT
    tm.employee_id,
    tm.directorate,
    tm.position AS role,
    tm.grade,
    tm.tgv_name,
    tm.tv_name,
    tm.baseline_score,
    tm.user_score,
    tm.tv_match_rate,
    ta.tgv_match_rate,
    fa.final_match_rate
FROM tv_match tm
LEFT JOIN tgv_agg ta USING (employee_id, tgv_name)
LEFT JOIN final_agg fa USING (employee_id)
ORDER BY fa.final_match_rate DESC, tm.employee_id, tm.tgv_name, tm.tv_name;
