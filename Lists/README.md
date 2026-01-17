# Lists - Data Files

This directory contains JSON data files for AI governance and tracking across Teledyne.

## Purpose

Centralized data storage replacing SharePoint lists for AI tool tracking, project portfolio management, and strategic initiative monitoring.

## 📁 Contents

| File | Description | Items | Version |
|------|-------------|-------|---------|
| [AI_Tool_Library.json](AI_Tool_Library.json) | Catalog of approved AI tools and applications | 73 tools | 2.0 |
| [AI_Tool_Library.csv](AI_Tool_Library.csv) | CSV export of tool library (synced during RUN CLEANUP) | 73 tools | 2.0 |
| [AI_Tool_Library_2026-01-16.csv](AI_Tool_Library_2026-01-16.csv) | Timestamped CSV snapshot (archived) | 73 tools | 2.0 |
| [AI_Project_Portfolio.json](AI_Project_Portfolio.json) | Tracking of AI projects and experiments | 19 projects | 2.0 |
| [AI_Project_Portfolio.csv](AI_Project_Portfolio.csv) | CSV export of project portfolio (synced during RUN CLEANUP) | 19 projects | 2.0 |
| [AI_Strategic_Initiatives.json](AI_Strategic_Initiatives.json) | C-level sponsored strategic AI programs | 7 initiatives | 1.1 |
| [AI_Strategic_Initiatives.csv](AI_Strategic_Initiatives.csv) | CSV export of strategic initiatives (synced during RUN CLEANUP) | 7 initiatives | 1.1 |
| [Org_Structure.json](Org_Structure.json) | Organizational hierarchy for business groups | 8 groups | 1.0 |
| [AI_Project_Activity_2026-01-16.json](AI_Project_Activity_2026-01-16.json) | Project activity tracking snapshot | 7 projects | 1.0 |

## 📊 Data Structure

All JSON files follow a consistent structure:

```json
{
  "fieldOptions": {
    "fieldName": [
      {
        "value": "Option Value",
        "description": "Explanation of option"
      }
    ]
  },
  "items": [ /* array of data items */ ],
  "metadata": {
    "version": "x.x",
    "lastUpdated": "YYYY-MM-DD",
    "totalItems": 0,
    "description": "File purpose"
  }
}
```

## 🔑 Key Fields

### AI_Tool_Library.json
- **toolId**: Unique identifier (TL###)
- **oldSharePointId**: Reference to original SharePoint list item
- **category**: Tool classification (Code Assistant, Productivity, etc.)
- **status**: Approval status (Approved, Pilot, Under Review, etc.)
- **vendor**: Tool provider (Microsoft, OpenAI, Google, etc.)

### AI_Project_Portfolio.json
- **projectId**: Unique identifier (AP###)
- **oldSharePointId**: Reference to original SharePoint list item
- **businessSegment**: Teledyne segment owning the project
- **projectType**: Classification (Custom Solution, POC, Tool Integration, etc.)
- **status**: Current state (Ideation, In Development, Pilot, In Production, etc.)
- **stage**: Maturity level (Explore, Build, Pilot, Scale, Sunset)

### AI_Strategic_Initiatives.json
- **initiativeId**: Unique identifier (SI###)
- **oldSharePointId**: Reference to original SharePoint list item
- **executiveSponsor**: C-level executive sponsoring the initiative
- **strategicObjective**: Primary business goal
- **riskLevel**: Assessment (Low, Medium, High)
- **complianceRequirements**: Regulatory requirements (SOC2, GDPR, DFARS, etc.)

## 🔄 Migration from SharePoint

These files replaced SharePoint lists. The `oldSharePointId` field maintains traceability to original list items.

## ✏️ Editing Guidelines

1. **Always update metadata**: Increment version and update `lastUpdated` date
2. **Maintain field options**: Ensure values match `fieldOptions` definitions
3. **Validate JSON**: Use a JSON validator before committing changes
4. **Sequential IDs**: Use next available ID for new items (e.g., TL006, AP021, SI004)

## 📝 Usage Examples

### Query by Status
```javascript
const activePilots = projects.filter(p => p.status === "Pilot");
```

### Get Tools by Vendor
```javascript
const microsoftTools = tools.filter(t => t.vendor === "Microsoft");
```

### Calculate Total Investment
```javascript
const totalInvestment = initiatives.reduce((sum, i) => sum + i.investment, 0);
```

## Navigation

- [← Back to Root](../README.md)
- [Flowcharts](../Flowcharts/README.md) - Process diagrams
- [Forms](../Forms/README.md) - Assessment templates
- [.github](../.github/README.md) - Agent instructions

---

*For schema details and field descriptions, see individual JSON files.*
