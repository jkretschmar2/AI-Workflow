# To-Do List

## Priority: Diagram & Visualization Enhancements

### High-Level AI Governance Flowchart
- [ ] Create simplified high-level flowchart for AI approvals (executive summary view)
- [ ] Create governance framework visual diagram showing roles, responsibilities, and decision authorities
- [ ] Create associated governance artifacts (RACI matrix, approval matrix, escalation paths)

### Scoring & Analytics Visualizations
- [ ] Update `quadrantChart.mmd` with scoring methodology for:
  - [ ] AI Tools (e.g., Risk vs. Value, Effort vs. Impact)
  - [ ] AI Projects (e.g., Strategic Alignment vs. Feasibility)
  - [ ] Strategic Initiatives (e.g., Investment vs. Return timeline)
- [ ] Document scoring criteria and axis definitions

### Pipeline Flow Visualization
- [ ] Update `sankey.mmd` to show flow through pipeline:
  - [ ] Tool requests → Review stages → Approval/Rejection
  - [ ] Project lifecycle → Phase transitions → Outcomes
  - [ ] Strategic initiatives → Resource allocation → Deliverables
- [ ] Connect to actual data counts from JSON files

### File Reorganization
- [ ] Rename `Process flow.mmd` to better represent full pipeline context (e.g., `AI Governance Pipeline.mmd` or `AI Request Lifecycle.mmd`)
  - [ ] Update all references in README files
  - [ ] Update subprocess file references
  - [ ] Update docs/ static site references
- [ ] Remove `Journey AI.mmd` (deprecated - no longer needed)
  - [x] Remove from Flowcharts/
  - [x] Remove from docs/data/
  - [x] Update Flowcharts/README.md

## Priority: Web & Intranet Development

### Interactive HTML Site Updates
- [ ] Update `docs/` site to reflect current project state:
  - [ ] Add governance framework visualization
  - [ ] Add quadrant chart with scoring methodology
  - [ ] Add sankey pipeline flow diagram
  - [ ] Update navigation for new/renamed files
  - [ ] Improve mobile responsiveness
- [ ] Add interactive filtering/search for tool library

### Intranet Design Project
- [ ] Create `Intranet/` folder for intranet design artifacts
- [ ] Add wireframes and mockups
- [ ] Capture UX/UI ideas and requirements
- [ ] Document integration points with existing systems
- [ ] Create style guide and branding assets

## Priority: Microsoft 365 & SharePoint Integration

### Planner & Task Management
- [ ] Add links to Microsoft Planner for all list items (Tools, Projects, Initiatives)
- [ ] Create to-do trackers with Microsoft Graph API integrations
- [ ] Implement Power Automate flows for task synchronization

### SharePoint Forms & Workflows
- [ ] Implement new AI Tool Request form on SharePoint
- [ ] Create Microsoft Forms version for external/simplified submissions
- [ ] Set up approval workflow automation
- [ ] Connect forms to AI_Tool_Library.json data

### ServiceNow Integration
- [ ] Get ServiceNow access and permissions
- [ ] Document current ServiceNow AI-related workflows and automations
- [ ] Migrate/replicate ServiceNow automations to Power Automate
- [ ] Map ServiceNow catalog items to new SharePoint forms
- [ ] Create transition plan for moving from ServiceNow to M365

## Priority: Governance & Organizational Artifacts

### RACI Charts
- [ ] Create RACI chart for Tool Request process
- [ ] Create RACI chart for Project Approval workflow
- [ ] Create RACI chart for Strategic Initiative governance
- [ ] Create RACI chart for Risk Assessment reviews
- [ ] Create master RACI matrix covering all major activities

### Organizational Structure
- [ ] Create org chart for AI Governance Committee
- [ ] Document reporting relationships and escalation paths
- [ ] Map roles to Org_Structure.json data

### Risk Management
- [ ] Update risk management framework with ISO 31000 references
- [ ] Add ISO/IEC 27001 security risk specifications
- [ ] Reference ISO/IEC 42001 (AI Management System) standards
- [ ] Create risk register template aligned with ISO specs

## Priority: Workstream Blueprints

### Main Workstreams (Blueprints)
- [ ] Create blueprint for Workstream 1: AI Tool Evaluation & Approval
- [ ] Create blueprint for Workstream 2: AI Project Lifecycle Management
- [ ] Create blueprint for Workstream 3: Strategic AI Initiative Governance
- [ ] Create blueprint for Workstream 4: Continuous Monitoring & Compliance
- [ ] Document dependencies and handoffs between workstreams

## Priority: Reporting & Analytics

### Power BI Reporting
- [ ] Create Power BI report for tracking all AI activity
- [ ] Dashboard views: Tools, Projects, Initiatives, Risk
- [ ] Connect to JSON data sources (or synced CSV files)
- [ ] Add trend analysis and status indicators

### KPI Framework
- [ ] Define KPI list with the following structure:
  | KPI Name | What We Track | How We Track | Data Source | Target Value |
  |----------|---------------|--------------|-------------|--------------|
- [ ] Create KPI tracking spreadsheet/dashboard
- [ ] Identify leading vs. lagging indicators
- [ ] Set up automated data collection where possible

## Priority: Vendor & Project Tracking

### Palantir Follow-up
- [ ] Create Palantir activity status tracker
- [ ] Document evaluation progress and outcomes
- [ ] Track action items and next steps
- [ ] Log communications and meeting notes

### LDP Projects
- [ ] Create `LDP Projects/` folder structure
- [ ] Create subfolder: LDP Project 1 - [Name]
- [ ] Create subfolder: LDP Project 2 - [Name]
- [ ] Create subfolder: LDP Project 3 - [Name]
- [ ] Add project artifacts, status reports, and deliverables

### Claude AI Project
- [ ] Document Claude project activity and experiments
- [ ] Track prompt engineering patterns
- [ ] Log use cases and outcomes
- [ ] Capture lessons learned and best practices

## AI Tool Library

- [ ] Review tool fields in JSON to align with original table schema
  - [ ] Verify all original fields are present (Orig ID, Tool Name, Category, etc.)
  - [ ] Check data types match requirements (Number, Text, Dropdown, Currency, etc.)
  - [ ] Validate "Valid Values / Notes" constraints are enforced
  - [ ] Ensure required fields are marked appropriately

## Process Flow Documentation

- [ ] Validate all external links in Process flow.mmd
- [ ] Verify sequence numbering is continuous in all phases

## Repository Maintenance

- [ ] Commit current changes
- [ ] Push updates to GitHub
- [ ] Consider adding GitHub Actions for validation

## Future Enhancements

- [ ] Create schema validation for AI_Tool_Library.json
- [ ] Add template for AI Risk Assessment submissions
- [ ] Document relationship between Tool Library and Process Flow
- [ ] Create visual dashboard/report from Tool Library data

### Knowledge Management
- [ ] Implement [Zettelkasten method](https://zettelkasten.de/overview/) for notetaking
  - [ ] Create atomic notes structure (one idea per note)
  - [ ] Implement unique ID system for notes
  - [ ] Build linking system between related notes
  - [ ] Create index/hub notes for major topics
  - [ ] Evaluate tools: Obsidian, Notion, or folder-based approach

---

*Last Updated: 2026-01-16*
