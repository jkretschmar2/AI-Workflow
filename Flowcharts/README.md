# Flowcharts

This directory contains Mermaid diagram files documenting the AI Software Request governance process.

## Files

| File | Description | Type |
|------|-------------|------|
| [Process flow.mmd](Process%20flow.mmd) | Complete AI software request lifecycle (8 phases: 0-7) | Flowchart |
| [quadrantChart.mmd](quadrantChart.mmd) | Example: Campaign reach/engagement analysis | Quadrant Chart |
| [sankey.mmd](sankey.mmd) | Example: Request flow visualization | Sankey Diagram |

## Diagram Conventions

### Phase Color Coding

Each phase uses consistent color coding:

| Phase | Color | Hex Code |
|-------|-------|----------|
| Inputs | Blue | `#4A90E2` |
| Request | Purple | `#7B4397` |
| Interest | Teal | `#1B9B8E` |
| Demo | Light Blue | `#00A0E9` |
| Pilot | Gold | `#D4A017` |
| Formal | Magenta | `#945491` |
| Implementation | Dark Blue | `#1E3A5F` |
| Evaluation | Green | `#7CB342` |
| Exit/Notification | Red | `#FF7F7F` |

### Numbering Convention

Steps follow Phase.Step format:
- `1.1`, `1.2` - Request phase steps
- `2.1`, `2.2` - Interest phase steps
- etc.

## Viewing Diagrams

### VS Code
Install the [Mermaid Preview](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid) extension and use the preview pane.

### GitHub
GitHub natively renders Mermaid in markdown. Wrap content in:
```
```mermaid
<diagram code>
```
```

### Online
Use [Mermaid Live Editor](https://mermaid.live/) to visualize and edit.

## Maintenance

When updating diagrams:
1. Follow the sequence numbering convention
2. Maintain color consistency per phase
3. Update cross-references in related diagrams
4. Test rendering before committing
