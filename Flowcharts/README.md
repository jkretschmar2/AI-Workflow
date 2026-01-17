# Flowcharts - Process Diagrams

This directory contains Mermaid flowchart files documenting AI governance and project workflows.

## Purpose

Visual documentation of the AI Software Request governance process using Mermaid diagram-as-code. These diagrams provide:
- **Process clarity** - Step-by-step visualization of approval workflows
- **Stakeholder alignment** - Clear understanding of roles and decision points
- **Maintainability** - Version-controlled, text-based diagrams that are easy to update

## 📊 Contents

| File | Description | Type | Phases |
|------|-------------|------|--------|
| [Process flow.mmd](Process%20flow.mmd) | Complete AI request lifecycle | Flowchart | 8 phases (0-7) |
| [quadrantChart.mmd](quadrantChart.mmd) | Campaign reach/engagement analysis | Quadrant chart | Example |
| [sankey.mmd](sankey.mmd) | Flow visualization example | Sankey diagram | Example |

### Subprocess Detail Diagrams

| File | Parent Phase | Description |
|------|--------------|-------------|
| [1.10 Initial IT and Security Review.mmd](1.10%20Initial%20IT%20and%20Security%20Review.mmd) | Request Phase | Security requirements and compliance assessment |
| [2.1 AI Board Review.mmd](2.1%20AI%20Board%20Review.mmd) | Interest Phase | Multi-business interest evaluation and strategic alignment |
| [3.3 Pilot Cost Approval by Requestor.mmd](3.3%20Pilot%20Cost%20Approval%20by%20Requestor.mmd) | Demo Phase | Pilot budget approval and cost negotiation |
| [3.4 IT Security Approval.mmd](3.4%20IT%20Security%20Approval.mmd) | Demo Phase | IT infrastructure and security controls review |
| [3.5 AI Governance Legal Compliance Ethics Approval.mmd](3.5%20AI%20Governance%20Legal%20Compliance%20Ethics%20Approval.mmd) | Demo Phase | Legal, compliance, ethics, and data privacy assessment |
| [3.7 Approval Split Cost Between Interested.mmd](3.7%20Approval%20Split%20Cost%20Between%20Interested.mmd) | Demo Phase | Multi-business cost allocation agreement |
| [5.1 AI Board Review.mmd](5.1%20AI%20Board%20Review.mmd) | Formal Request | Post-pilot board review for production approval |
| [5.2 AI Governance Committee Review.mmd](5.2%20AI%20Governance%20Committee%20Review.mmd) | Formal Request | Governance committee approval for deployment |
| [5.6 Teledyne Senior Leadership Review.mmd](5.6%20Teledyne%20Senior%20Leadership%20Review.mmd) | Formal Request | Executive leadership review for enterprise deployment |
| [6.1 Architecture Review by ITSS Business Vendor.mmd](6.1%20Architecture%20Review%20by%20ITSS%20Business%20Vendor.mmd) | Implementation | Technical architecture validation and design approval |
| [6.5 Production Deployment.mmd](6.5%20Production%20Deployment.mmd) | Implementation | Production system deployment and go-live process |

## Navigation

- [← Back to Root](../README.md)
- [Lists](../Lists/README.md) - JSON data files
- [Forms](../Forms/README.md) - Assessment templates
- [.github](../.github/README.md) - Agent instructions

## 🔄 AI Software Request Process

The main [Process flow.mmd](../Process%20flow.mmd) documents the complete lifecycle:

### Phase 0: Required Inputs
Prerequisites and documentation before submission

### Phase 1: Request Phase (1.1-1.13)
- Request submission (Email/Portal/ServiceNow)
- Type classification (Product vs Function)
- Initial IT & Security review
- Denied list check

### Phase 2: Interest Phase (2.1-2.5)
- AI Board review
- Multi-business interest evaluation
- Single business approval decision

### Phase 3: Demo Phase (3.1-3.13)
- Vendor demonstration scheduling
- Stakeholder alignment
- Cost, IT, Security, and Governance approvals
- Cost allocation for multi-business pilots

### Phase 4: Pilot Phase (4.1-4.5)
- Success criteria definition
- Pilot execution with vendor
- Results evaluation

### Phase 5: Formal Request (5.1-5.11)
- AI Board and Governance Committee review
- Business case development
- Senior leadership approval
- Single vs Enterprise-wide deployment decision

### Phase 6: Implementation (6.1-6.6)
- Architecture review
- Procurement
- Implementation and testing
- User acceptance testing
- Production deployment

### Phase 7: Continuous Evaluation (7.1-7.5)
- Periodic success criteria review
- Continued need assessment
- Service decommissioning (if needed)

## 🎨 Diagram Conventions

### Color Coding
Each phase uses consistent colors for visual clarity:
- **Inputs**: Blue (#4A90E2)
- **Request**: Purple (#7B4397)
- **Interest**: Teal (#1B9B8E)
- **Demo**: Sky Blue (#00A0E9)
- **Pilot**: Gold (#D4A017)
- **Formal**: Magenta (#945491)
- **Implementation**: Dark Blue (#1E3A5F)
- **Evaluation**: Green (#7CB342)
- **Exit/Notification**: Red (#FF7F7F)

### Node Shapes
- `Document`: @{ shape: doc }
- `Input/Start`: [/"text"/]
- `Process`: ("text")
- `Decision`: {"text"}
- `Exit/Notification`: (["text"])
- `Phase Transition`: @{ shape: delay }

## 📝 Maintenance Guidelines

See [.github/AGENTS.md](../.github/AGENTS.md) for detailed instructions on:
- Sequence number management
- Color consistency rules
- Link validation
- Cross-file reference updates

## 🔗 Related Documentation

- [README.md](../README.md) - Repository overview
- [.github/AGENTS.md](../.github/AGENTS.md) - Agent maintenance instructions
- [.github/copilot-instructions.md](../.github/copilot-instructions.md) - AI assistant guidelines

---

*For diagram updates, follow the conventions in AGENTS.md to maintain consistency.*
