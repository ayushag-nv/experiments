# OpenHands + AgentLLM (claude-3.7-sonnet) + EnvLLM (gpt-4o)

OpenHands (0.28.1) is backed by claude-3-7-sonnet-20250219

Environment (LLM-as-colleague & LLM-as-evaluator) uses gpt-4o-2024-08-06

Evaluated all 41 tasks that involve colleagues (NPCs) backed by GPT4o model

# Evaluation Results Report

## Results per File

*Sorted by score (⭐ indicates perfect completion)*

| Filename | Total | Result | Score | Steps | Cost |
|----------|--------|---------|-------|-------|------|
| admin-ask-for-meeting-feedback-image | 6 | 6 | 1.00 ⭐ | 33 | 3.70 |
| admin-ask-for-upgrade-reimbursement-image | 4 | 4 | 1.00 ⭐ | 40 | 7.37 |
| admin-employee-info-reconciliation-image | 7 | 7 | 1.00 ⭐ | 29 | 3.06 |
| hr-check-for-invalid-passwords-and-ask-for-valid-passwords-image | 4 | 4 | 1.00 ⭐ | 34 | 3.07 |
| hr-collect-feedbacks-image | 5 | 5 | 1.00 ⭐ | 25 | 2.31 |
| hr-collect-multiple-valid-passwords-image | 4 | 4 | 1.00 ⭐ | 44 | 7.85 |
| hr-delete-and-insert-user-image | 3 | 3 | 1.00 ⭐ | 29 | 5.48 |
| hr-get-valid-password-image | 4 | 4 | 1.00 ⭐ | 20 | 1.43 |
| hr-new-grad-job-description-2-image | 4 | 4 | 1.00 ⭐ | 29 | 3.24 |
| hr-new-grad-job-description-3-image | 5 | 5 | 1.00 ⭐ | 36 | 4.83 |
| hr-pick-interviewer-1-image | 6 | 6 | 1.00 ⭐ | 29 | 4.23 |
| pm-ask-issue-assignee-for-issue-status-and-update-in-plane-image | 3 | 3 | 1.00 ⭐ | 28 | 4.31 |
| pm-check-backlog-update-issues-image | 5 | 5 | 1.00 ⭐ | 22 | 2.60 |
| pm-prepare-meeting-with-customers-image | 6 | 6 | 1.00 ⭐ | 20 | 2.00 |
| pm-schedule-meeting-1-image | 5 | 5 | 1.00 ⭐ | 25 | 2.19 |
| pm-send-notification-to-corresponding-user-image | 4 | 4 | 1.00 ⭐ | 28 | 2.94 |
| qa-update-issue-status-according-to-colleagues-image | 6 | 6 | 1.00 ⭐ | 23 | 1.61 |
| sde-reply-community-issue-by-asking-npc-image | 5 | 5 | 1.00 ⭐ | 24 | 4.71 |
| admin-get-best-vendor-quote-image | 6 | 4 | 0.33 | 48 | 7.94 |
| hr-green-card-consultation-image | 3 | 2 | 0.33 | 33 | 5.42 |
| hr-pick-interviewer-2-image | 6 | 4 | 0.33 | 26 | 2.51 |
| sde-create-new-repo-image | 3 | 2 | 0.33 | 40 | 7.57 |
| example-image | 5 | 3 | 0.30 | 60 | 11.28 |
| finance-find-signatories-image | 5 | 3 | 0.30 | 52 | 11.43 |
| admin-check-employees-budget-and-reply-2-image | 4 | 2 | 0.25 | 42 | 6.72 |
| admin-check-employees-budget-and-reply-image | 4 | 2 | 0.25 | 48 | 9.34 |
| hr-check-attendance-multiple-days-department-with-chat-image | 4 | 2 | 0.25 | 46 | 10.23 |
| hr-resume-screening-image | 4 | 2 | 0.25 | 43 | 8.70 |
| pm-plan-personnel-for-new-project-image | 7 | 3 | 0.21 | 34 | 4.01 |
| pm-ask-for-issue-and-create-in-gitlab-image | 5 | 2 | 0.20 | 48 | 7.65 |
| pm-schedule-meeting-2-image | 5 | 2 | 0.20 | 24 | 1.99 |
| sde-find-answer-in-codebase-3-image | 5 | 2 | 0.20 | 39 | 7.71 |
| admin-check-employees-budget-and-reply-and-record-image | 6 | 2 | 0.17 | 46 | 9.92 |
| admin-collect-requests-and-compute-total-price-image | 4 | 1 | 0.12 | 54 | 9.41 |
| finance-r-d-activities-image | 6 | 1 | 0.08 | 36 | 7.08 |
| hr-mass-survey-image | 7 | 1 | 0.07 | 39 | 8.43 |
| finance-apply-tax-credit-image | 8 | 0 | 0.00 | 33 | 4.61 |
| hr-pick-interviewer-3-image | 4 | 0 | 0.00 | 16 | 0.84 |
| sde-create-new-gitlab-project-logo-image | 3 | 0 | 0.00 | 32 | 4.09 |
| sde-debug-crashed-server-image | 8 | 0 | 0.00 | 100 | 7.76 |
| sde-report-agent-repos-image | 2 | 0 | 0.00 | 6 | 0.22 |

## Summary

**Tasks Evaluated:** 41

**Perfect Completions:** 18/41 (43.90%)

**Overall Score:** 54.13%

**Average Steps:** 35.68

**Average Cost (USD):** 5.41


## Statistics

| Metric | Value |
|---------|--------|
| Highest Task Score | 100.00% |
| Lowest Task Score | 0.00% |
| Median Task Score | 33.33% |
| Average Task Score | 54.13% |

## Statistics per Nature Category

| Metric | Value |
|---------|--------|
| Perfect Completions for sde | 1 (16.67%) |
| Average Score for sde | 25.56% |
| Perfect Completions for pm | 5 (62.50%) |
| Average Score for pm | 70.18% |
| Perfect Completions for ds | 0 (0.00%) |
| Average Score for ds | 0.00% |
| Perfect Completions for admin | 3 (37.50%) |
| Average Score for admin | 51.56% |
| Perfect Completions for hr | 8 (57.14%) |
| Average Score for hr | 65.99% |
| Perfect Completions for finance | 0 (0.00%) |
| Average Score for finance | 12.78% |
| Perfect Completions for other | 1 (50.00%) |
| Average Score for other | 65.00% |

## Statistics per Service Category

| Metric | Value |
|---------|--------|
| Perfect Completions for gitlab | 2 (25.00%) |
| Average Score for gitlab | 37.92% |
| Perfect Completions for plane | 3 (100.00%) |
| Average Score for plane | 100.00% |
| Perfect Completions for rocketchat | 18 (43.90%) |
| Average Score for rocketchat | 54.13% |
| Perfect Completions for owncloud | 4 (22.22%) |
| Average Score for owncloud | 37.93% |
