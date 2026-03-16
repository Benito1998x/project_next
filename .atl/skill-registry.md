# Skill Registry - project_next

> Generated: 2026-03-16
> Mode: engram

## Global Skills (user-level)

| Skill | Trigger | Location |
|-------|---------|----------|
| sdd-verify | When the orchestrator launches you to verify a completed (or partially completed) change. | `C:\Users\PC\.config\opencode\skills\sdd-verify\SKILL.md` |
| sdd-tasks | When the orchestrator launches you to create or update the task breakdown for a change. | `C:\Users\PC\.config\opencode\skills\sdd-tasks\SKILL.md` |
| sdd-spec | When the orchestrator launches you to write or update specs for a change. | `C:\Users\PC\.config\opencode\skills\sdd-spec\SKILL.md` |
| sdd-propose | When the orchestrator launches you to create or update a proposal for a change. | `C:\Users\PC\.config\opencode\skills\sdd-propose\SKILL.md` |
| sdd-init | When user wants to initialize SDD in a project, or says "sdd init", "iniciar sdd", "openspec init". | `C:\Users\PC\.config\opencode\skills\sdd-init\SKILL.md` |
| sdd-explore | When the orchestrator launches you to think through a feature, investigate the codebase, or clarify requirements. | `C:\Users\PC\.config\opencode\skills\sdd-explore\SKILL.md` |
| sdd-design | When the orchestrator launches you to write or update the technical design for a change. | `C:\Users\PC\.config\opencode\skills\sdd-design\SKILL.md` |
| sdd-archive | When the orchestrator launches you to archive a change after implementation and verification. | `C:\Users\PC\.config\opencode\skills\sdd-archive\SKILL.md` |
| sdd-apply | When the orchestrator launches you to implement one or more tasks from a change. | `C:\Users\PC\.config\opencode\skills\sdd-apply\SKILL.md` |
| go-testing | When writing Go tests, using teatest, or adding test coverage. | `C:\Users\PC\.config\opencode\skills\go-testing\SKILL.md` |
| skill-creator | When user asks to create a new skill, add agent instructions, or document patterns for AI. | `C:\Users\PC\.config\opencode\skills\skill-creator\SKILL.md` |

## Project Skills

| Skill | Trigger | Location | Status |
|-------|---------|----------|--------|
| `bpae-context` | Always load when working on project_next | `.agent/skills/bpae-context/SKILL.md` | ✅ Active |
| `bpae-fastapi` | When writing FastAPI endpoints in project_next | `.agent/skills/bpae-fastapi/SKILL.md` | ✅ Active |
| `bpae-supabase` | When working with Supabase in project_next | `.agent/skills/bpae-supabase/SKILL.md` | ✅ Active |

### Planned Skills

| Skill | Sprint | Purpose |
|-------|--------|---------|
| `bpae-prompts` | Sprint 2 | MiniMax prompt engineering |
| `bpae-generation` | Sprint 2 | Text generation service patterns |
| `bpae-prompts` | Sprint 2 | MiniMax prompt engineering |
| `bpae-generation` | Sprint 2 | Text generation service patterns |
| `bpae-investigador` | Sprint 3 | Research agent workflow |
| `bpae-pestel` | Sprint 3 | PESTEL analysis generation |
| `bpae-encuesta` | Sprint 4 | Survey design methodology |
| `bpae-mercado` | Sprint 4 | Market analysis patterns |
| `bpae-excel-maestro` | Sprint 5 | Excel master template handling |
| `bpae-coherence` | Sprint 5 | Financial validation rules |
| `bpae-compiler` | Sprint 6 | Document compilation |
| `bpae-word-plantilla` | Sprint 6 | Word template styling |
| `bpae-deployment` | Sprint 7 | Oracle Cloud deployment |
| `bpae-troubleshooting` | Sprint 7 | Common errors and solutions |

## Project Conventions

| File | Purpose |
|------|---------|
| `project/plan_implementacion_v2.md` | Plan de implementación completo del proyecto BPAE |
| `docs/indice-completo.md` | Índice completo de plan de negocio (referencia teórica) |
| `docs/indice-mvp.md` | Índice MVP priorizado para desarrollo en 23 días |
| `docs/README.md` | Guía rápida de uso de los índices |
| `docs/indice-detallado/indice-mvp-detallado.md` | Guía experta detallada por sección (MVP) |
| `docs/indice-detallado/indice-completo-detallado.md` | Guía experta completa (referencia) |
| `docs/indice-esquema/esquema-mvp.md` | Esquema de datos MVP (solo esencial) |
| `docs/indice-esquema/esquema-completo.md` | Esquema de datos completo (todas las tablas) |

## Commands (OpenCode)

| Command | Description |
|---------|-------------|
| `/sdd-init` | Initialize SDD context in a project |
| `/sdd-new` | Create a new SDD change proposal |
| `/sdd-continue` | Continue with the next artifact in the SDD workflow |
| `/sdd-ff` | Fast-forward: proposal → spec → design → tasks |
| `/sdd-apply` | Implement tasks from a change |
| `/sdd-verify` | Verify implementation against specs |
| `/sdd-archive` | Archive a completed change |

## Persistence Backend

**Mode**: engram

- Project context saved to: `sdd-init/project_next`
- Use `mem_search` to retrieve project context
- Use `mem_save` to persist decisions and architecture

## Next Steps

1. Create project-level skills in `.agent/skills/` or `.claude/skills/`
2. Run `/sdd-explore <topic>` to investigate features
3. Run `/sdd-new <change-name>` to start a new change proposal