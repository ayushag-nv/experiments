# OpenHands + AgentLLM (claude-3.7-sonnet) + EnvLLM (deepseek v3)

OpenHands (0.28.1) is backed by claude-3-7-sonnet-20250219

Environment (LLM-as-colleague & LLM-as-evaluator) uses DeepSeek v3

Evaluated all 41 tasks that involve colleagues (NPCs) backed by DeepSeek-v3 model

# Evaluation Results Report

## Results per File

*Sorted by score (⭐ indicates perfect completion)*

| Filename | Total | Result | Score | Steps | Cost |
|----------|--------|---------|-------|-------|------|
| admin-ask-for-meeting-feedback-image | 6 | 6 | 1.00 ⭐ | 36 | 4.44 |
| admin-ask-for-upgrade-reimbursement-image | 4 | 4 | 1.00 ⭐ | 37 | 6.60 |
| admin-employee-info-reconciliation-image | 7 | 7 | 1.00 ⭐ | 27 | 2.67 |
| hr-collect-feedbacks-image | 5 | 5 | 1.00 ⭐ | 25 | 2.31 |
| hr-collect-multiple-valid-passwords-image | 4 | 4 | 1.00 ⭐ | 29 | 3.44 |
| hr-get-valid-password-image | 4 | 4 | 1.00 ⭐ | 24 | 1.96 |
| hr-new-grad-job-description-3-image | 5 | 5 | 1.00 ⭐ | 29 | 3.22 |
| hr-pick-interviewer-1-image | 6 | 6 | 1.00 ⭐ | 34 | 5.94 |
| pm-ask-for-issue-and-create-in-gitlab-image | 5 | 5 | 1.00 ⭐ | 35 | 5.69 |
| pm-ask-issue-assignee-for-issue-status-and-update-in-plane-image | 3 | 3 | 1.00 ⭐ | 20 | 2.72 |
| pm-check-backlog-update-issues-image | 5 | 5 | 1.00 ⭐ | 22 | 3.18 |
| pm-schedule-meeting-1-image | 5 | 5 | 1.00 ⭐ | 30 | 3.24 |
| pm-schedule-meeting-2-image | 5 | 5 | 1.00 ⭐ | 22 | 1.68 |
| pm-send-notification-to-corresponding-user-image | 4 | 4 | 1.00 ⭐ | 34 | 4.39 |
| qa-update-issue-status-according-to-colleagues-image | 6 | 6 | 1.00 ⭐ | 23 | 1.63 |
| sde-create-new-repo-image | 3 | 3 | 1.00 ⭐ | 37 | 6.07 |
| pm-prepare-meeting-with-customers-image | 6 | 5 | 0.42 | 20 | 1.86 |
| hr-check-attendance-multiple-days-department-with-chat-image | 4 | 3 | 0.38 | 41 | 7.73 |
| hr-new-grad-job-description-2-image | 4 | 3 | 0.38 | 30 | 3.17 |
| hr-delete-and-insert-user-image | 3 | 2 | 0.33 | 28 | 5.21 |
| hr-green-card-consultation-image | 3 | 2 | 0.33 | 35 | 5.80 |
| hr-pick-interviewer-2-image | 6 | 4 | 0.33 | 26 | 2.48 |
| sde-create-new-gitlab-project-logo-image | 3 | 2 | 0.33 | 33 | 4.60 |
| example-image | 5 | 3 | 0.30 | 62 | 11.38 |
| finance-find-signatories-image | 5 | 3 | 0.30 | 41 | 6.70 |
| sde-reply-community-issue-by-asking-npc-image | 5 | 3 | 0.30 | 13 | 1.65 |
| admin-check-employees-budget-and-reply-2-image | 4 | 2 | 0.25 | 41 | 6.62 |
| admin-collect-requests-and-compute-total-price-image | 4 | 2 | 0.25 | 33 | 4.75 |
| admin-get-best-vendor-quote-image | 6 | 3 | 0.25 | 42 | 7.50 |
| hr-check-for-invalid-passwords-and-ask-for-valid-passwords-image | 4 | 2 | 0.25 | 26 | 2.49 |
| hr-resume-screening-image | 4 | 2 | 0.25 | 49 | 10.08 |
| pm-plan-personnel-for-new-project-image | 7 | 3 | 0.21 | 40 | 5.89 |
| admin-check-employees-budget-and-reply-and-record-image | 6 | 2 | 0.17 | 44 | 9.14 |
| admin-check-employees-budget-and-reply-image | 4 | 1 | 0.12 | 33 | 4.53 |
| hr-pick-interviewer-3-image | 4 | 1 | 0.12 | 16 | 0.84 |
| sde-debug-crashed-server-image | 8 | 2 | 0.12 | 100 | 12.05 |
| hr-mass-survey-image | 7 | 1 | 0.07 | 26 | 3.62 |
| finance-apply-tax-credit-image | 8 | 0 | 0.00 | 26 | 3.65 |
| finance-r-d-activities-image | 6 | 0 | 0.00 | 26 | 4.21 |
| sde-find-answer-in-codebase-3-image | 5 | 0 | 0.00 | 34 | 6.65 |
| sde-report-agent-repos-image | 2 | 0 | 0.00 | 6 | 0.22 |

## Summary

**Tasks Evaluated:** 41

**Perfect Completions:** 16/41 (39.02%)

**Overall Score:** 52.38%

**Average Steps:** 32.56

**Average Cost (USD):** 4.68


## Statistics

| Metric | Value |
|---------|--------|
| Highest Task Score | 100.00% |
| Lowest Task Score | 0.00% |
| Median Task Score | 33.33% |
| Average Task Score | 52.38% |

## Statistics per Nature Category

| Metric | Value |
|---------|--------|
| Perfect Completions for sde | 1 (16.67%) |
| Average Score for sde | 29.31% |
| Perfect Completions for pm | 6 (75.00%) |
| Average Score for pm | 82.89% |
| Perfect Completions for ds | 0 (0.00%) |
| Average Score for ds | 0.00% |
| Perfect Completions for admin | 3 (37.50%) |
| Average Score for admin | 50.52% |
| Perfect Completions for hr | 5 (35.71%) |
| Average Score for hr | 53.19% |
| Perfect Completions for finance | 0 (0.00%) |
| Average Score for finance | 10.00% |
| Perfect Completions for other | 1 (50.00%) |
| Average Score for other | 65.00% |

## Statistics per Service Category

| Metric | Value |
|---------|--------|
| Perfect Completions for gitlab | 2 (25.00%) |
| Average Score for gitlab | 41.88% |
| Perfect Completions for plane | 3 (100.00%) |
| Average Score for plane | 100.00% |
| Perfect Completions for rocketchat | 16 (39.02%) |
| Average Score for rocketchat | 52.38% |
| Perfect Completions for owncloud | 3 (16.67%) |
| Average Score for owncloud | 33.12% |
