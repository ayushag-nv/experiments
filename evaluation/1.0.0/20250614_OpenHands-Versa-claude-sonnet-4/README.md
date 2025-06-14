
<div align="center">
  <h1 align="center">OpenHands-Versa: Coding Agents with Multimodal Browsing are Generalist Problem Solvers</h1>
  <img src="https://raw.githubusercontent.com/adityasoni9998/OpenHands-Versa/main/docs/static/img/OpenHands-Versa.png" width="900">
</div>

OpenHands-Versa is a versatilte, generalist, multimodal agent built on top of the popular OpenHands framework. This agent addresses the crucial challenge of generalizability faced by several prior agentic frameworks. We augment OpenHands with more capabilities like multimodal browsing, multimodal document understanding and web search. Check out our [paper](https://arxiv.org/abs/2506.03011) for more details about our work!

OpenHands-Versa is available open-source for future research and is also integrated into the upstream [OpenHands](https://github.com/all-Hands-AI/OpenHands/) repository. This submission corresponds to the version of OpenHands-Versa reported in our original research paper. Our code and experimental scripts are available open-source [here](https://github.com/adityasoni9998/OpenHands-Versa).

# Evaluation Results Report (Claude-Sonnet-4)

## Results per File

*Sorted by score (⭐ indicates perfect completion)*

| Filename | Total | Result | Score | Steps | Cost (assuming no prompt caching)|
|----------|--------|---------|-------|-------|------|
| admin-ask-for-upgrade-reimbursement-image | 4 | 4 | 1.00 ⭐ | 50 | 0.90 |
| admin-check-employees-budget-and-reply-and-record-image | 6 | 6 | 1.00 ⭐ | 89 | 1.85 |
| ds-fix-table-values-and-missing-answers-image | 6 | 6 | 1.00 ⭐ | 53 | 1.92 |
| ds-sql-exercise-image | 6 | 6 | 1.00 ⭐ | 15 | 0.33 |
| finance-check-attendance-payroll-image | 3 | 3 | 1.00 ⭐ | 85 | 3.08 |
| hr-check-attendance-one-day-image | 3 | 3 | 1.00 ⭐ | 40 | 1.05 |
| hr-check-for-invalid-passwords-and-ask-for-valid-passwords-image | 4 | 4 | 1.00 ⭐ | 25 | 0.63 |
| hr-collect-feedbacks-image | 5 | 5 | 1.00 ⭐ | 23 | 0.41 |
| hr-collect-multiple-valid-passwords-image | 4 | 4 | 1.00 ⭐ | 46 | 0.93 |
| hr-delete-and-insert-user-image | 3 | 3 | 1.00 ⭐ | 35 | 0.60 |
| hr-get-valid-password-image | 4 | 4 | 1.00 ⭐ | 22 | 0.62 |
| hr-make-slides-introduce-leadership-image | 5 | 5 | 1.00 ⭐ | 11 | 0.30 |
| hr-new-grad-job-description-2-image | 4 | 4 | 1.00 ⭐ | 45 | 0.92 |
| hr-new-grad-job-description-3-image | 5 | 5 | 1.00 ⭐ | 43 | 0.96 |
| hr-new-grad-job-description-image | 3 | 3 | 1.00 ⭐ | 37 | 1.00 |
| hr-pick-interviewer-1-image | 6 | 6 | 1.00 ⭐ | 46 | 0.79 |
| pm-add-new-moderator-image | 3 | 3 | 1.00 ⭐ | 23 | 0.40 |
| pm-ask-issue-assignee-for-issue-status-and-update-in-plane-image | 3 | 3 | 1.00 ⭐ | 19 | 0.33 |
| pm-create-channel-message-image | 3 | 3 | 1.00 ⭐ | 11 | 0.19 |
| pm-create-channel-message-medium-image | 6 | 6 | 1.00 ⭐ | 36 | 0.62 |
| pm-create-channel-new-leader-image | 3 | 3 | 1.00 ⭐ | 44 | 0.80 |
| pm-create-plane-issue-image | 2 | 2 | 1.00 ⭐ | 7 | 0.12 |
| pm-schedule-meeting-1-image | 5 | 5 | 1.00 ⭐ | 16 | 0.32 |
| pm-schedule-meeting-2-image | 5 | 5 | 1.00 ⭐ | 19 | 0.36 |
| pm-send-notification-to-corresponding-user-image | 4 | 4 | 1.00 ⭐ | 25 | 0.43 |
| pm-update-plane-issue-from-gitlab-status-image | 7 | 7 | 1.00 ⭐ | 12 | 0.23 |
| pm-update-project-milestones-image | 5 | 5 | 1.00 ⭐ | 19 | 0.33 |
| qa-update-issue-status-according-to-colleagues-image | 6 | 6 | 1.00 ⭐ | 20 | 0.36 |
| sde-add-wiki-page-image | 4 | 4 | 1.00 ⭐ | 28 | 0.51 |
| sde-change-license-easy-image | 4 | 4 | 1.00 ⭐ | 25 | 2.42 |
| sde-change-license-hard-image | 3 | 3 | 1.00 ⭐ | 27 | 1.43 |
| sde-close-an-issue-image | 2 | 2 | 1.00 ⭐ | 5 | 0.09 |
| sde-collect-open-issues-image | 3 | 3 | 1.00 ⭐ | 8 | 0.20 |
| sde-copilot-arena-server-easy-add-suffix-image | 4 | 4 | 1.00 ⭐ | 23 | 1.84 |
| sde-copilot-arena-server-new-endpoint-image | 9 | 9 | 1.00 ⭐ | 22 | 2.01 |
| sde-copilot-arena-server-setup-image | 7 | 7 | 1.00 ⭐ | 30 | 2.25 |
| sde-copy-issues-to-plane-image | 2 | 2 | 1.00 ⭐ | 15 | 0.26 |
| sde-create-new-characters-image | 4 | 4 | 1.00 ⭐ | 37 | 2.59 |
| sde-create-new-release-image | 2 | 2 | 1.00 ⭐ | 11 | 0.20 |
| sde-delete-stale-branch-image | 2 | 2 | 1.00 ⭐ | 8 | 0.13 |
| sde-dependency-change-1-image | 5 | 5 | 1.00 ⭐ | 18 | 1.18 |
| sde-find-answer-in-codebase-1-image | 3 | 3 | 1.00 ⭐ | 9 | 0.14 |
| sde-find-answer-in-codebase-2-image | 3 | 3 | 1.00 ⭐ | 39 | 0.69 |
| sde-fix-factual-mistake-image | 3 | 3 | 1.00 ⭐ | 7 | 0.13 |
| sde-install-go-image | 2 | 2 | 1.00 ⭐ | 10 | 0.19 |
| sde-install-openjdk-image | 2 | 2 | 1.00 ⭐ | 10 | 0.30 |
| sde-issue-label-management-image | 1 | 1 | 1.00 ⭐ | 9 | 0.16 |
| sde-milestone-meeting-image | 5 | 5 | 1.00 ⭐ | 25 | 0.45 |
| sde-pitch-idea-to-manager-image | 5 | 5 | 1.00 ⭐ | 27 | 0.96 |
| sde-reply-community-issue-with-fixed-reply-image | 3 | 3 | 1.00 ⭐ | 9 | 0.14 |
| sde-report-unit-test-coverage-to-plane-image | 4 | 4 | 1.00 ⭐ | 14 | 0.72 |
| sde-run-linter-on-openhands-image | 2 | 2 | 1.00 ⭐ | 28 | 1.66 |
| sde-sotopia-create-agent-image | 5 | 5 | 1.00 ⭐ | 29 | 1.90 |
| sde-summarize-recent-issues-image | 4 | 4 | 1.00 ⭐ | 20 | 0.35 |
| sde-sync-from-origin-repo-image | 1 | 1 | 1.00 ⭐ | 42 | 3.17 |
| sde-update-dev-document-image | 4 | 4 | 1.00 ⭐ | 26 | 1.26 |
| sde-update-issue-status-on-plane-image | 3 | 3 | 1.00 ⭐ | 14 | 0.24 |
| sde-write-a-unit-test-for-search_file-function-image | 5 | 5 | 1.00 ⭐ | 19 | 1.85 |
| sde-create-sqlite-database-image | 8 | 7 | 0.44 | 73 | 2.15 |
| admin-employee-info-reconciliation-image | 7 | 6 | 0.43 | 33 | 0.73 |
| pm-prepare-meeting-with-customers-image | 6 | 5 | 0.42 | 21 | 0.53 |
| ds-organise-report-sus-data-image | 5 | 4 | 0.40 | 86 | 1.49 |
| sde-write-a-unit-test-for-append_file-function-image | 5 | 4 | 0.40 | 32 | 4.39 |
| sde-write-a-unit-test-for-scroll_down-function-image | 5 | 4 | 0.40 | 37 | 5.04 |
| finance-expense-validation-image | 4 | 3 | 0.38 | 73 | 2.28 |
| pm-copy-plane-issues-to-gitlab-image | 4 | 3 | 0.38 | 14 | 0.26 |
| pm-monthly-attendance-slides-image | 4 | 3 | 0.38 | 74 | 1.60 |
| pm-update-sprint-cycles-image | 4 | 3 | 0.38 | 37 | 0.71 |
| sde-move-bustub-wiki-image | 4 | 3 | 0.38 | 19 | 0.43 |
| sde-run-all-unit-test-image | 4 | 3 | 0.38 | 26 | 1.57 |
| admin-get-best-vendor-quote-image | 6 | 4 | 0.33 | 67 | 1.92 |
| hr-green-card-consultation-image | 3 | 2 | 0.33 | 71 | 1.24 |
| hr-pick-interviewer-2-image | 6 | 4 | 0.33 | 25 | 0.50 |
| pm-change-channel-ownership-image | 3 | 2 | 0.33 | 17 | 0.28 |
| pm-update-gitlab-issue-from-plane-status-image | 3 | 2 | 0.33 | 9 | 0.17 |
| qa-escalate-emergency-image | 3 | 2 | 0.33 | 17 | 0.30 |
| sde-create-new-repo-image | 3 | 2 | 0.33 | 57 | 1.19 |
| sde-move-page-to-cloud-image | 3 | 2 | 0.33 | 26 | 0.95 |
| example-image | 5 | 3 | 0.30 | 25 | 0.77 |
| finance-find-signatories-image | 5 | 3 | 0.30 | 87 | 3.09 |
| pm-assign-issues-image | 5 | 3 | 0.30 | 59 | 1.05 |
| pm-present-gitlab-info-as-ppt-image | 5 | 3 | 0.30 | 19 | 0.60 |
| pm-send-hello-message-image | 5 | 3 | 0.30 | 5 | 0.09 |
| sde-reply-community-issue-by-asking-npc-image | 5 | 3 | 0.30 | 13 | 0.22 |
| admin-check-employees-budget-and-reply-2-image | 4 | 2 | 0.25 | 90 | 1.60 |
| admin-check-employees-budget-and-reply-image | 4 | 2 | 0.25 | 58 | 1.02 |
| admin-collect-requests-and-compute-total-price-image | 4 | 2 | 0.25 | 48 | 0.88 |
| ds-find-meeting-spreadsheet-image | 2 | 1 | 0.25 | 37 | 1.11 |
| ds-visualize-data-in-pie-and-bar-chart-image | 4 | 2 | 0.25 | 77 | 2.44 |
| finance-create-10k-income-report-image | 6 | 3 | 0.25 | 90 | 2.77 |
| finance-substantial-presence-test-image | 2 | 1 | 0.25 | 10 | 0.24 |
| hr-check-attendance-multiple-days-image | 4 | 2 | 0.25 | 47 | 1.51 |
| hr-create-career-ladder-image | 4 | 2 | 0.25 | 69 | 2.11 |
| hr-resume-screening-image | 4 | 2 | 0.25 | 90 | 1.57 |
| pm-distribute-information-image | 2 | 1 | 0.25 | 13 | 0.24 |
| pm-monitor-new-bug-issues-image | 4 | 2 | 0.25 | 24 | 0.44 |
| sde-change-branch-policy-image | 2 | 1 | 0.25 | 39 | 0.70 |
| sde-check-high-priority-issue-image | 4 | 2 | 0.25 | 15 | 0.27 |
| sde-find-api-image | 4 | 2 | 0.25 | 39 | 1.85 |
| hr-analyze-outing-bills-image | 7 | 3 | 0.21 | 84 | 2.40 |
| pm-plan-personnel-for-new-project-image | 7 | 3 | 0.21 | 90 | 1.81 |
| hr-massive-resume-screening-image | 5 | 2 | 0.20 | 79 | 1.56 |
| pm-create-teammate-channel-from-spreadsheet-image | 5 | 2 | 0.20 | 89 | 2.23 |
| pm-projects-analytics-image | 5 | 2 | 0.20 | 8 | 0.15 |
| sde-fix-rising-wave-datatype-image | 5 | 2 | 0.20 | 35 | 2.68 |
| admin-ask-for-meeting-feedback-image | 6 | 2 | 0.17 | 39 | 0.85 |
| admin-read-survey-and-summarise-image | 3 | 1 | 0.17 | 89 | 1.54 |
| admin-remove-pages-pdf-image | 3 | 1 | 0.17 | 64 | 2.22 |
| hr-transfer-group-image | 3 | 1 | 0.17 | 27 | 0.47 |
| sde-sotopia-update-ci-image | 3 | 1 | 0.17 | 19 | 0.72 |
| hr-populate-salary-increase-memo-image | 7 | 2 | 0.14 | 90 | 1.55 |
| finance-budget-variance-image | 4 | 1 | 0.12 | 53 | 1.70 |
| finance-revenue-reconciliation-image | 4 | 1 | 0.12 | 90 | 3.24 |
| hr-check-attendance-multiple-days-department-with-chat-image | 4 | 1 | 0.12 | 90 | 1.54 |
| hr-create-employee-manual-image | 4 | 1 | 0.12 | 90 | 1.69 |
| hr-organize-talent-info-image | 4 | 1 | 0.12 | 59 | 1.20 |
| hr-pick-interviewer-3-image | 4 | 1 | 0.12 | 7 | 0.13 |
| hr-resume-categorization-image | 4 | 1 | 0.12 | 63 | 3.14 |
| sde-debug-crashed-server-image | 8 | 2 | 0.12 | 71 | 5.69 |
| sde-implement-buffer-pool-manager-bustub-image | 12 | 3 | 0.12 | 61 | 11.99 |
| sde-migrate-package-manager-image | 8 | 2 | 0.12 | 38 | 2.28 |
| sde-troubleshoot-dev-setup-image | 4 | 1 | 0.12 | 20 | 0.42 |
| ds-answer-spreadsheet-questions-image | 5 | 1 | 0.10 | 90 | 2.64 |
| pm-ask-for-issue-and-create-in-gitlab-image | 5 | 1 | 0.10 | 30 | 0.53 |
| pm-check-backlog-update-issues-image | 5 | 1 | 0.10 | 18 | 0.33 |
| bm-classify-nationality-image | 6 | 1 | 0.08 | 90 | 1.51 |
| ds-janusgraph-exercise-image | 6 | 1 | 0.08 | 62 | 10.24 |
| finance-r-d-activities-image | 6 | 1 | 0.08 | 90 | 1.83 |
| sde-create-commit-table-for-all-gitlab-users-image | 6 | 1 | 0.08 | 17 | 0.90 |
| sde-implement-hyperloglog-image | 6 | 1 | 0.08 | 63 | 10.28 |
| sde-run-janusgraph-image | 6 | 1 | 0.08 | 55 | 10.77 |
| hr-mass-survey-image | 7 | 1 | 0.07 | 90 | 2.01 |
| sde-sotopia-dev-container-image | 7 | 1 | 0.07 | 30 | 0.55 |
| research-reproduce-figures-image | 8 | 1 | 0.06 | 90 | 1.61 |
| hr-internal-tooling-slides-image | 10 | 1 | 0.05 | 83 | 2.34 |
| admin-arrange-meeting-rooms-image | 2 | 0 | 0.00 | 10 | 0.28 |
| admin-make-spreadsheet-image | 5 | 0 | 0.00 | 90 | 1.67 |
| admin-mass-forms-filling-image | 5 | 0 | 0.00 | 57 | 1.25 |
| admin-translate-sales-chat-image | 4 | 0 | 0.00 | 90 | 1.52 |
| admin-watch-video-image | 2 | 0 | 0.00 | 62 | 1.25 |
| ds-answer-numerical-data-question-image | 6 | 0 | 0.00 | 90 | 1.98 |
| ds-calculate-spreadsheet-stats-image | 5 | 0 | 0.00 | 90 | 1.54 |
| ds-coffee-shop-database-management-image | 10 | 0 | 0.00 | 85 | 3.63 |
| ds-format-excel-sheets-image | 4 | 0 | 0.00 | 56 | 1.71 |
| ds-merge-multiple-sheets-image | 3 | 0 | 0.00 | 90 | 1.53 |
| ds-predictive-modeling-image | 3 | 0 | 0.00 | 35 | 0.84 |
| ds-stock-analysis-slides-image | 8 | 0 | 0.00 | 83 | 3.18 |
| finance-apply-tax-credit-image | 8 | 0 | 0.00 | 78 | 3.99 |
| finance-invoice-matching-image | 5 | 0 | 0.00 | 90 | 1.81 |
| finance-nonqualified-bill-ask-for-reimburse-image | 2 | 0 | 0.00 | 62 | 1.14 |
| finance-qualified-bill-ask-for-reimburse-image | 5 | 0 | 0.00 | 90 | 1.53 |
| hr-check-attendance-multiple-days-department-image | 3 | 0 | 0.00 | 76 | 2.03 |
| hr-salary-analysis-image | 2 | 0 | 0.00 | 51 | 1.21 |
| ml-generate-gradcam-image | 4 | 0 | 0.00 | 73 | 1.89 |
| ml-grade-exam-image | 8 | 0 | 0.00 | 90 | 1.65 |
| pm-present-engineer-group-members-image | 3 | 0 | 0.00 | 87 | 2.67 |
| research-answer-questions-on-paper-image | 12 | 0 | 0.00 | 90 | 1.60 |
| sde-add-all-repos-to-docs-image | 7 | 0 | 0.00 | 90 | 1.60 |
| sde-add-one-gitlab-pipeline-image | 3 | 0 | 0.00 | 5 | 0.09 |
| sde-check-and-run-unit-test-image | 2 | 0 | 0.00 | 33 | 2.29 |
| sde-close-all-gitlab-issues-image | 2 | 0 | 0.00 | 58 | 1.02 |
| sde-close-all-issue-on-all-project-under-tac-workspace-image | 3 | 0 | 0.00 | 90 | 1.73 |
| sde-close-all-prs-image | 2 | 0 | 0.00 | 63 | 1.12 |
| sde-copy-table-from-pdf-to-xlsx-image | 5 | 0 | 0.00 | 90 | 3.82 |
| sde-create-new-gitlab-project-logo-image | 3 | 0 | 0.00 | 43 | 0.92 |
| sde-delete-all-project-under-plane-image | 1 | 0 | 0.00 | 59 | 1.18 |
| sde-delete-all-repos-image | 1 | 0 | 0.00 | 90 | 1.64 |
| sde-find-answer-in-codebase-3-image | 5 | 0 | 0.00 | 90 | 1.97 |
| sde-implement-covering-index-in-janusgraph-image | 3 | 0 | 0.00 | 75 | 13.04 |
| sde-implement-raft-in-go-image | 10 | 0 | 0.00 | 68 | 9.11 |
| sde-repo_profile_pic-image | 3 | 0 | 0.00 | 24 | 0.92 |
| sde-report-agent-repos-image | 2 | 0 | 0.00 | 38 | 0.66 |
| sde-run-rising-wave-locally-image | 2 | 0 | 0.00 | 90 | 1.60 |
| sde-sotopia-create-agent-wo-repo-image | 6 | 0 | 0.00 | 35 | 2.72 |
| sde-update-readme-image | 2 | 0 | 0.00 | 22 | 0.37 |

## Summary

**Tasks Evaluated:** 175

**Perfect Completions:** 58/175 (33.14%)

**Overall Score:** 43.19%

**Average Steps:** 46.45

**Average Cost (USD):** 1.63


## Statistics

| Metric | Value |
|---------|--------|
| Highest Task Score | 100.00% |
| Lowest Task Score | 0.00% |
| Median Task Score | 25.00% |
| Average Task Score | 43.19% |

## Statistics per Nature Category

| Metric | Value |
|---------|--------|
| Perfect Completions for sde | 30/69 (43.48%) |
| Average Score for sde | 50.57% |
| Perfect Completions for pm | 11/28 (39.29%) |
| Average Score for pm | 55.08% |
| Perfect Completions for ds | 2/14 (14.29%) |
| Average Score for ds | 22.02% |
| Perfect Completions for admin | 2/15 (13.33%) |
| Average Score for admin | 26.75% |
| Perfect Completions for hr | 11/29 (37.93%) |
| Average Score for hr | 47.89% |
| Perfect Completions for finance | 1/12 (8.33%) |
| Average Score for finance | 20.90% |
| Perfect Completions for other | 1/8 (12.50%) |
| Average Score for other | 22.24% |