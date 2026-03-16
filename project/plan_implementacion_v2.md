# Plan de Implementación v2.0: Business Plan Automation Engine
### Ricardo construye. La IA asiste con el Gentleman Stack. Ricardo aprende.
**Nextstat 2026 | SCRUM | LLM: MiniMax 2.5 | Dev Agent: Claude Code + Gentleman Stack**

---

## La Filosofía que Gobierna Todo

```
Ricardo es Tony Stark.
Claude Code es Jarvis.
Los sub-agentes son el equipo especialista.

NO: "La IA programa por mí"
SÍ: "Yo programo CON la IA, entendiendo cada decisión"

Si Ricardo no puede explicar por qué hizo algo,
no está aprendiendo. Está ejecutando instrucciones.
```

---

## El Cambio Fundamental: El Entorno de Desarrollo

Antes de hablar de sprints hay que entender qué herramienta usa Ricardo para construir.

```
ANTES (plan v1):
Ricardo escribe código en un editor
Le pregunta cosas a Claude.ai
La IA responde en el chat
Ricardo copia y entiende

AHORA (plan v2 con Gentleman Stack):
Ricardo usa Claude Code como agente de desarrollo
Claude Code tiene:
→ engram: memoria persistente entre sesiones de trabajo
→ SDD workflow: proceso estructurado por feature
→ SKILL.md del proyecto: el agente sabe exactamente
  cómo debe construir cada parte del Business Plan Engine
→ Persona orientada a enseñar: el agente explica antes de hacer

La diferencia: el agente recuerda el proyecto entre días,
sigue un workflow disciplinado y actúa como senior developer
que enseña, no como autocomplete glorificado.
```

---

## Stack Completo del Proyecto

```
ENTORNO DE DESARROLLO (cómo Ricardo construye):
├── Claude Code          → agente de desarrollo principal
├── gentle-ai            → instalador del Gentleman ecosystem
├── engram               → memoria persistente del agente de dev
├── agent-teams-lite     → patrón SDD (Spec-Driven Development)
└── Gentleman-Skills     → skills del proyecto (SKILL.md por módulo)

PRODUCTO (lo que Ricardo construye):
├── LLM: MiniMax 2.5    → única API de LLM del sistema
├── Backend: FastAPI     → Python, ya en el stack
├── DB: Supabase         → PostgreSQL + Storage + Auth
├── Frontend MVP: Streamlit → interfaz para Ricardo (especialista)
├── Word: python-docx    → manipulación de documentos Word
├── Excel: openpyxl      → manipulación de planillas Excel
├── Búsqueda: Tavily API → web search del Agente Investigador
├── Caché: Redis         → sesiones activas
├── KB: ChromaDB         → Knowledge Base vectorial
└── Infra: Oracle Cloud Free Tier → deployment
```

---

## FASE 0: Configuración del Entorno y Fundamentos
### Duración: 1.5 semanas | Prerequisito absoluto

```
OBJETIVO:
Ricardo tiene su entorno de desarrollo profesional configurado
y entiende los conceptos base antes de escribir una línea de código.

El entorno no es opcional. Un carpintero no trabaja sin taller.
```

### Paso 0.1 — Instalar el Gentleman Stack

```
TAREA: Instalar gentle-ai y configurar Claude Code

Conceptos a investigar ANTES de instalar:
→ "Qué es Claude Code y cómo funciona"
→ "Qué es un agente de IA de desarrollo"
→ "Qué es gentle-ai Gentleman Programming"

Instalación:
irm https://raw.githubusercontent.com/Gentleman-Programming/gentle-ai/main/scripts/install.ps1 | powershell

Componentes a instalar:
→ Claude Code (el agente de desarrollo)
→ engram (memoria persistente)
→ agent-teams-lite (workflow SDD)
→ Gentleman-Skills base
→ Persona de enseñanza

VERIFICACIÓN:
El agente de Claude Code puede responder:
"¿Qué es el SDD workflow y cuál es tu rol en él?"
Si no puede, la instalación no está completa.
```

### Paso 0.2 — Entender engram

```
Conceptos a investigar:
→ "Qué es la memoria persistente en agentes IA"
→ "engram Gentleman-Programming cómo funciona"
→ "mem_save mem_search engram tutorial"

PRÁCTICA:
Iniciar una sesión con Claude Code.
Pedirle que guarde en engram:
"Recuerda que este proyecto es el Business Plan Automation Engine
de Nextstat, construido por Ricardo Nogales, con FastAPI + Supabase
+ MiniMax 2.5 + python-docx + openpyxl"

Cerrar Claude Code. Abrir de nuevo.
Preguntarle: "¿Qué proyecto estamos construyendo?"
Si recuerda: engram funciona.
Si no recuerda: revisar la configuración.
```

### Paso 0.3 — Entender SDD (Spec-Driven Development)

```
Conceptos a investigar:
→ "Spec-Driven Development explained"
→ "agent-teams-lite workflow SDD Gentleman"
→ "orquestador sub-agentes IA patrón"

El ciclo SDD que Ricardo usará en CADA feature:

/sdd:explore "idea de la feature"
    → El agente piensa, no crea archivos
    → Ricardo entiende el enfoque antes de comprometerse

/sdd:new "nombre-del-cambio"
    → El agente genera: spec.md + design.md + tasks.md
    → Ricardo revisa y aprueba cada artefacto
    → NO se escribe código hasta que Ricardo aprueba el diseño

/sdd:apply
    → El agente implementa fase por fase
    → Ricardo revisa cada fase antes de continuar
    → Si algo no se entiende: PARAR y preguntar

/sdd:verify
    → El agente verifica que la implementación cumple la spec
    → Corre tests si existen

REGLA DE ORO:
Ricardo NUNCA aprueba un artefacto SDD que no entiende.
"Está bien, continúa" sin entender = no está aprendiendo.
```

### Paso 0.4 — Crear las Skills del Proyecto

```
Conceptos a investigar:
→ "SKILL.md format Agent Skills standard"
→ "cómo crear un skill para Claude Code"
→ "Gentleman-Skills skill-creator"

TAREA:
Crear el primer SKILL.md del proyecto:

.claude/skills/bpae-context/SKILL.md

Este skill le dice al agente:
→ Qué es el Business Plan Automation Engine
→ El stack tecnológico del proyecto
→ Las convenciones de código del proyecto
→ Las reglas de negocio clave
→ Cómo está organizado el proyecto

Este skill se carga automáticamente en cada sesión.
El agente nunca olvida el contexto del proyecto.
```

### Conceptos Fundamentales — Fase 0

```
SEMANA 1:

1. "Qué es una API REST y cómo funciona"
   Entender: endpoints, HTTP methods, request/response, status codes

2. "Qué es JSON y cómo se estructura"
   Entender: objetos, arrays, tipos de datos, anidamiento

3. "Qué es una base de datos relacional"
   Entender: tablas, relaciones, primary key, foreign key, SQL básico

4. "Qué es un LLM: tokens, contexto, temperatura, system prompt"
   Entender: cómo funciona MiniMax 2.5 a nivel conceptual

5. "Qué es el patrón cliente-servidor"
   Entender: frontend ↔ backend ↔ DB

SEMANA 1.5:

6. "Git workflow: commit, branch, merge, pull request"
   Entender: por qué versionamos el código

7. "Qué es Docker y por qué se usa"
   Entender: contenedores, imagen, docker-compose

8. "Qué es Claude Code y el SDD workflow"
   Ver: documentación de agent-teams-lite

ENTREGABLE DE FASE 0:
Ricardo dibuja en papel la arquitectura completa del sistema.
Explica cada componente con sus propias palabras.
No puede avanzar si no puede hacer esto.
```

---

## SPRINT 1: El Esqueleto — Primera Sesión SDD
### Duración: 2 semanas | Primera vez que Ricardo usa SDD completo

```
OBJETIVO:
Al final de este sprint existe:
→ El proyecto Python estructurado según las convenciones del proyecto
→ FastAPI con un endpoint que llama a MiniMax 2.5
→ Supabase configurado con las tablas base
→ Streamlit con una pantalla de inicio
→ engram tiene el contexto del proyecto guardado
→ El primer SKILL.md del proyecto creado y funcionando

CÓMO SE TRABAJA EN ESTE SPRINT:
Todo se hace con el ciclo SDD. Ricardo nunca escribe código
sin antes haber pasado por explore → spec → design → tasks.
```

### Sesión SDD 1.1 — Estructura del Proyecto

```
Ricardo le dice a Claude Code:
/sdd:explore "estructura profesional para proyecto FastAPI + Supabase + Streamlit"

El agente propone la estructura.
Ricardo la estudia, hace preguntas hasta entenderla.
Cuando Ricardo la entiende y está de acuerdo:

/sdd:new "project-scaffold"
→ spec.md: qué debe tener la estructura
→ design.md: por qué cada carpeta existe
→ tasks.md: qué crear paso a paso

Ricardo lee CADA artefacto. Si no entiende algo, pregunta.
Solo cuando aprueba los tres:

/sdd:apply
→ El agente crea la estructura
→ Ricardo verifica que entiende para qué sirve cada archivo
```

### Conceptos a Investigar — Sprint 1

```
SEMANA 1:

1. "Estructura de proyectos Python profesional"
   Buscar: "Python project structure best practices 2024"
   Aplicar: Entender por qué se separan api/, services/, models/, db/

2. "FastAPI tutorial oficial completo"
   Buscar: documentación fastapi.tiangolo.com
   Aplicar: Decoradores @app.get/@app.post, Pydantic models

3. "Variables de entorno en Python con python-dotenv"
   Buscar: "python-dotenv tutorial"
   Aplicar: Configurar .env con credenciales MiniMax y Supabase

4. "MiniMax API documentation Python"
   Buscar: documentación oficial MiniMax API
   Aplicar: Primera llamada desde Python, entender el response

SEMANA 2:

5. "Supabase Python client supabase-py"
   Buscar: documentación supabase-py
   Aplicar: insert, select, update desde Python

6. "Streamlit getting started tutorial"
   Buscar: docs.streamlit.io
   Aplicar: st.write, st.button, st.text_input, st.session_state

7. "Git conventional commits"
   Buscar: "conventional commits specification"
   Aplicar: feat:, fix:, docs:, refactor: en todos los commits
```

### Skills a Crear en Este Sprint

```
.claude/skills/bpae-context/SKILL.md
→ Contexto completo del proyecto para el agente

.claude/skills/bpae-fastapi/SKILL.md
→ Convenciones de FastAPI del proyecto:
  cómo nombrar endpoints, cómo estructurar responses,
  cómo manejar errores, qué Pydantic models usar

.claude/skills/bpae-supabase/SKILL.md
→ Convenciones de Supabase del proyecto:
  nombres de tablas, columnas estándar,
  cómo hacer queries, cómo manejar errores de DB
```

### Manipulación Word/Excel — Sprint 1

```
INVESTIGACIÓN WORD (Semana 1):
Buscar: "python-docx tutorial completo oficial"
Entender:
→ Crear documento desde cero
→ Agregar título con estilo Heading 1, Heading 2
→ Agregar párrafo con texto normal
→ Agregar tabla básica (3 columnas, 5 filas)
→ Guardar como .docx

SDD PARA WORD:
/sdd:explore "script de práctica python-docx que crea un documento básico"
→ Spec: qué debe contener el documento de prueba
→ Design: qué funciones de python-docx usar y por qué
→ Apply: el agente escribe el script
→ Ricardo lo estudia línea por línea hasta entenderlo todo

INVESTIGACIÓN EXCEL (Semana 2):
Buscar: "openpyxl tutorial completo"
Entender:
→ Crear archivo con múltiples hojas
→ Escribir valores en celdas
→ Escribir fórmulas (=SUM, =AVERAGE, referencias entre hojas)
→ Aplicar estilos básicos
→ Guardar archivo

SDD PARA EXCEL:
/sdd:explore "script de práctica openpyxl con Panel de Control y fórmulas"
→ El agente explica el concepto del Panel de Control
→ Ricardo entiende por qué las fórmulas no deben tener valores hardcodeados
→ Solo entonces: /sdd:apply
```

### Entregable Verificable Sprint 1

```
CHECKLIST TÉCNICO:
□ Estructura de carpetas creada y entendida
□ FastAPI responde en /health con {status: "ok"}
□ Se puede crear un plan en Supabase via POST /planes
□ Streamlit lista los planes desde Supabase
□ MiniMax responde a un prompt de prueba
□ practice_word.py genera .docx con título, párrafo y tabla
□ practice_excel.py genera .xlsx con Panel de Control y fórmulas
□ Todo en GitHub con commits convencionales

CHECKLIST DE APRENDIZAJE (el más importante):
□ Ricardo puede explicar qué hace cada endpoint de FastAPI
□ Ricardo puede explicar qué es Pydantic y por qué se usa
□ Ricardo puede explicar qué es session_state en Streamlit
□ Ricardo puede explicar por qué las fórmulas usan referencias de celda
□ Ricardo usó el ciclo SDD completo al menos 3 veces

engram debe tener guardado:
→ La decisión de estructura del proyecto
→ Las convenciones acordadas de FastAPI
→ Las convenciones acordadas de Supabase
```

---

## SPRINT 2: Motor de Generación — Primera Sección Real
### Duración: 2 semanas | Primera sección del plan generada con MiniMax

```
OBJETIVO:
El sistema genera la Sección 2 (Definición del Negocio) completa.
Ricardo entiende: prompt engineering, structured output, servicio de generación.
```

### Conceptos a Investigar — Sprint 2

```
SEMANA 1:

1. "Prompt engineering guide 2024"
   Buscar: promptingguide.ai
   Entender: system prompt, user prompt, few-shot examples,
             chain of thought, structured output

2. "Cómo obtener JSON estructurado de un LLM"
   Buscar: "structured output LLM JSON format"
   Entender: por qué los LLMs a veces rompen el formato
   Entender: cómo forzar JSON válido siempre

3. "Markdown sintaxis completa"
   Buscar: "markdown cheatsheet"
   Entender: el agente genera en Markdown, luego se convierte a Word

4. "Python manejo de errores try/except best practices"
   Buscar: "python exception handling guide"
   Aplicar: el cliente MiniMax nunca debe crashear el sistema

SEMANA 2:

5. "Repository pattern Python"
   Buscar: "repository pattern python tutorial"
   Entender: separar acceso a datos de lógica de negocio

6. "FastAPI Depends dependency injection"
   Buscar: "FastAPI dependency injection tutorial"
   Entender: para qué sirve, cómo inyectar la DB

7. "Streamlit forms y state management"
   Buscar: "streamlit st.form session_state advanced"
   Aplicar: formulario guiado para Sección 2
```

### Skills a Crear en Este Sprint

```
.claude/skills/bpae-prompts/SKILL.md
→ Cómo están estructuradas las instrucciones expertas del proyecto
→ El formato estándar de cada instrucción experta
→ Cómo inyectar variables en los prompts
→ Qué formato de JSON pedir a MiniMax y por qué

.claude/skills/bpae-generation/SKILL.md
→ Cómo funciona el servicio de generación
→ El ciclo: instrucción → prompt → MiniMax → parse → guardar
→ Cómo manejar errores de generación
→ Cuándo regenerar vs. cuándo ajustar manualmente
```

### Manipulación Word/Excel — Sprint 2

```
TÉCNICA CLAVE: Convertidor Markdown → Word

Buscar: "python-docx styles apply programmatically"
Buscar: "convert markdown elements to python-docx"
Entender:
→ Estilos Word: Normal, Heading1, Heading2, Heading3, List Bullet
→ Cómo aplicar negrita a texto específico dentro de un párrafo
→ Por qué el convertidor es mejor que pedir al LLM que genere XML

SDD PARA EL CONVERTIDOR:
/sdd:explore "convertidor de Markdown a python-docx"
→ El agente explica el approach
→ Ricardo entiende cada elemento a convertir:
  # → Heading1, ## → Heading2, **texto** → bold run
  - item → List Bullet, párrafo normal → Normal style
→ /sdd:new "markdown-to-docx-converter"
→ Spec, Design, Tasks → Ricardo aprueba cada uno
→ /sdd:apply → agente implementa
→ Ricardo estudia el código resultante línea por línea

engram guarda:
→ "El convertidor MD→Word usa este mapeo de estilos..."
→ "Decisión: no usamos python-mammoth porque..."
```

### Entregable Verificable Sprint 2

```
CHECKLIST:
□ El sistema genera Sección 2 completa con MiniMax 2.5
□ El output de MiniMax siempre es JSON válido (nunca falla el parse)
□ La sección se guarda en Supabase con estado correcto
□ Ricardo puede aprobar/rechazar/regenerar desde Streamlit
□ El convertidor MD→Word maneja: títulos, párrafos, listas, negritas
□ Una sección aprobada genera un .docx descargable

CHECKLIST DE APRENDIZAJE:
□ Ricardo puede explicar qué es un system prompt y para qué sirve
□ Ricardo puede explicar por qué pedimos JSON en lugar de texto libre
□ Ricardo puede escribir una instrucción experta nueva sin ayuda
□ Ricardo usó SDD para cada feature del sprint
```

---

## SPRINT 3: El Agente Investigador
### Duración: 2 semanas | PESTEL y Porter con datos reales de Bolivia

```
OBJETIVO:
El Agente Investigador busca datos reales en la web.
El sistema genera PESTEL y Porter con fuentes reales.
Ricardo entiende qué es un agente de IA y cómo se construye.
```

### Conceptos a Investigar — Sprint 3

```
SEMANA 1:

1. "Qué es un agente de IA: razonamiento, herramientas, ciclo de acción"
   Buscar: "AI agent explained simply tools actions"
   Buscar: "build simple AI agent Python from scratch no framework"
   IMPORTANTE: Ricardo construye el agente en Python puro primero.
   No LangChain todavía. Si no entiende qué hace el framework,
   no puede debuggearlo cuando falla.

2. "Qué es RAG Retrieval Augmented Generation"
   Buscar: "RAG explained simply for beginners"
   Entender: por qué un LLM solo no sabe datos actuales de Bolivia

3. "Tavily API para búsqueda web en agentes"
   Buscar: documentación oficial Tavily API
   Aplicar: primera búsqueda sobre sector en Bolivia desde Python

4. "Python asyncio async await tutorial"
   Buscar: "python asyncio beginner tutorial"
   Entender: por qué es útil para llamadas paralelas a APIs

SEMANA 2:

5. "Redis Python redis-py tutorial"
   Buscar: "redis-py getting started"
   Entender: set, get, expire, por qué cachear resultados de búsqueda
   Aplicar: cachear resultados de Tavily por 24 horas

6. "Cómo estructurar el research_pack JSON"
   Esta no es una búsqueda externa. Ricardo define la estructura
   del JSON que el Agente Investigador produce.
   Pregunta a Claude Code: "¿Qué debería contener el research_pack
   para que el agente de PESTEL pueda trabajar con él?"
   Estudia la respuesta, decide, documenta en engram.
```

### Skills a Crear en Este Sprint

```
.claude/skills/bpae-investigador/SKILL.md
→ Cómo funciona el Agente Investigador
→ El ciclo: queries → Tavily → cache Redis → síntesis MiniMax
→ El formato del research_pack.json
→ Qué busca primero (KB local) antes de ir a la web
→ Cómo citar fuentes en el research_pack

.claude/skills/bpae-pestel/SKILL.md
→ La instrucción experta completa del análisis PESTEL
→ Qué inputs necesita (research_pack + rubro + ciudad)
→ El formato exacto del JSON de output
→ Criterios de calidad del análisis
→ Errores comunes a evitar
→ Fuentes Bolivia: INE, BCB, Fundempresa, ASFI
```

### Manipulación Word/Excel — Sprint 3

```
TÉCNICA: Tablas con color condicional en Word

Buscar: "python-docx table cell background color"
Buscar: "python-docx table formatting borders"
Entender:
→ table.cell(fila, columna) para acceder a celda específica
→ Cómo cambiar color de fondo de una celda
→ Merge de celdas para headers

EJERCICIO SDD:
/sdd:explore "tabla PESTEL en Word con colores de impacto"
→ Spec: tabla con 6 filas, 4 columnas, colores por nivel de impacto
→ Design: qué funciones de python-docx usar para cada elemento
→ Apply: agente implementa, Ricardo estudia línea por línea
→ Resultado: la tabla PESTEL más profesional que Ricardo ha visto

engram guarda:
→ "Para colorear celda Word se usa: ..."
→ "Decisión de colores del PESTEL: ALTO=#FF4444, MEDIO=#FFD700, BAJO=#44BB44"
```

### Entregable Verificable Sprint 3

```
CHECKLIST:
□ El Agente Investigador busca datos reales con Tavily
□ Los resultados se cachean en Redis (verificado con redis-cli)
□ El PESTEL se genera con fuentes reales bolivianas
□ El Porter se genera con datos del sector específico
□ La tabla PESTEL en Word tiene colores condicionales por impacto
□ El Agente Investigador consulta la KB local antes de ir a la web

CHECKLIST DE APRENDIZAJE:
□ Ricardo puede explicar el ciclo de un agente (razonar→actuar→observar)
□ Ricardo puede explicar qué es RAG con un ejemplo concreto
□ Ricardo puede explicar por qué cacheamos y con qué TTL
□ Ricardo entiende por qué NO usamos LangChain aún
```

---

## SPRINT 4: El Núcleo — Investigación de Mercado y Encuesta
### Duración: 3 semanas | El sprint más importante del proyecto

```
OBJETIVO:
El sistema maneja el flujo completo de investigación de mercado:
encuesta generada → estado WAITING_SURVEY → resultados procesados
→ buyer persona real → TAM/SAM/SOM calculado → demanda validada.
```

### Conceptos a Investigar — Sprint 4

```
SEMANA 1:

1. "State Machine pattern Python"
   Buscar: "state machine python implementation simple"
   Entender: estados, transiciones, eventos
   Aplicar: los estados del plan (PENDING→ACTIVE→WAITING→APPROVED)

2. "FastAPI file upload UploadFile"
   Buscar: "FastAPI file upload tutorial"
   Entender: cómo recibir archivos Excel/CSV del usuario
   Aplicar: endpoint para subir resultados de encuesta

3. "Diseño metodológico de encuestas"
   Buscar: "survey design methodology best practices"
   Buscar: "Van Westendorp price sensitivity meter"
   Buscar: "Likert scale survey design"
   Entender: esto es de contenido, no de código.
   Si Ricardo no entiende el método, el skill de encuesta será malo.

SEMANA 2:

4. "Pandas tutorial completo para análisis de datos"
   Buscar: documentación oficial pandas
   Entender: DataFrame, read_excel, read_csv, value_counts(),
             groupby(), describe()
   Aplicar: procesar los resultados de la encuesta

5. "Estadística descriptiva en Python con pandas"
   Buscar: "descriptive statistics pandas tutorial"
   Entender: frecuencia, porcentaje, media, mediana, moda
   Aplicar: el procesador de encuesta genera estadísticas reales

6. "TAM SAM SOM calculation methods"
   Buscar: "TAM SAM SOM top-down bottom-up market sizing"
   Entender: los dos métodos y cuándo usar cada uno
   Aplicar: el sistema calcula ambos y los muestra

SEMANA 3:

7. "Supabase Storage Python file upload"
   Buscar: "supabase storage python tutorial"
   Entender: upload, download, URLs públicas/privadas
   Aplicar: guardar la encuesta Word y los resultados Excel
```

### Skills a Crear en Este Sprint

```
.claude/skills/bpae-encuesta/SKILL.md
→ Metodología de diseño de encuestas por rubro
→ Estructura del instrumento: segmentación, comportamiento, intención
→ Cómo calcular el tamaño de muestra
→ Cómo construir preguntas Van Westendorp
→ El formato del instrumento Word que debe generarse
→ Cómo procesar los resultados con pandas

.claude/skills/bpae-mercado/SKILL.md
→ Cómo calcular TAM/SAM/SOM con los dos métodos
→ Formato del buyer persona con datos duros y blandos
→ El research_pack.json de la investigación de mercado
→ Cómo cruzar datos primarios y secundarios
→ El JSON de handoff hacia el Agente Financiero
```

### Manipulación Word/Excel — Sprint 4

```
TÉCNICA WORD — Encuesta profesional imprimible:

Buscar: "python-docx page margins setup"
Buscar: "python-docx header footer page numbers"
Buscar: "python-docx numbered list ordered"
Entender:
→ Márgenes de página (para que la encuesta sea imprimible en carta)
→ Encabezado con nombre del negocio y logo
→ Pie de página con número de página
→ Listas numeradas para preguntas
→ Tabla de escala Likert: [ ] 1  [ ] 2  [ ] 3  [ ] 4  [ ] 5
→ Espacio en blanco para respuestas abiertas (líneas horizontales)

SDD:
/sdd:explore "generador de encuesta Word profesional imprimible"
→ Spec: instrumento con 10 preguntas, 3 tipos, imprimible en carta
→ Design: qué elementos de python-docx usar para cada tipo de pregunta
→ Apply: agente implementa, Ricardo estudia y entiende

TÉCNICA EXCEL — Lectura de resultados de encuesta:

Buscar: "pandas read_excel multiple sheets"
Buscar: "pandas value_counts percentage normalize"
Entender:
→ Leer un Excel que el usuario completó
→ Calcular frecuencias y porcentajes por columna
→ Generar tabla de resumen automáticamente
→ Manejar respuestas vacías o inválidas

SDD:
/sdd:explore "procesador de resultados de encuesta con pandas"
→ Input: Excel con 30 respuestas ficticias
→ Output: tabla de frecuencias, porcentajes, precio óptimo Van Westendorp
```

### Entregable Verificable Sprint 4

```
CHECKLIST:
□ El sistema genera encuesta Word descargable y profesional
□ El plan_state cambia a WAITING_SURVEY correctamente
□ El usuario puede subir un Excel con resultados
□ Pandas procesa los resultados y genera estadísticas reales
□ El buyer persona se construye con datos reales de la encuesta
□ El TAM/SAM/SOM se calcula con ambos métodos
□ El estado persiste: si se cierra y abre el sistema, el plan sigue en WAITING_SURVEY

CHECKLIST DE APRENDIZAJE:
□ Ricardo puede explicar qué es una state machine con un diagrama en papel
□ Ricardo puede explicar qué hace pandas con un DataFrame
□ Ricardo puede explicar la diferencia entre el método top-down y bottom-up
□ Ricardo entiende por qué el Van Westendorp da el precio óptimo
```

---

## SPRINT 5: El Motor Financiero — El Excel Maestro
### Duración: 3 semanas | El sprint más técnico

```
OBJETIVO:
La plantilla Excel financiera está diseñada y el sistema la llena
con los datos de los sprints anteriores.
VAN, TIR, Payback, Punto de equilibrio calculados correctamente.
```

### Conceptos a Investigar — Sprint 5

```
SEMANA 1:

1. "Flujo de caja proyectado plan de negocio"
   Buscar: "cash flow projection business plan tutorial"
   Entender: ingresos, egresos, saldo, flujo acumulado
   ANTES de diseñar el Excel, Ricardo debe entender qué calcula.

2. "VAN TIR ROI Payback explicados con ejemplos"
   Buscar: "NPV IRR payback explained examples"
   Buscar: "tasa de descuento Bolivia cómo calcularla"
   Entender: qué mide cada indicador, cómo interpretarlo
   ANTES de implementar, Ricardo debe saber leer los resultados.

3. "openpyxl cargar plantilla Excel existente y modificar"
   Buscar: "openpyxl load_workbook modify save"
   Buscar: "openpyxl named ranges read write"
   Entender: cómo cargar una plantilla .xlsx sin romper las fórmulas

SEMANA 2:

4. "openpyxl data_only read calculated values"
   Buscar: "openpyxl data_only limitation workaround"
   Entender: el problema de leer valores calculados de fórmulas
   Esta es una decisión técnica que Ricardo debe tomar:
   openpyxl data_only vs. xlwings vs. replicar fórmulas en Python.
   No hay respuesta única. Ricardo investiga las 3 opciones
   y decide cuál usar, documentando la razón en engram.

5. "Punto de equilibrio fórmula unidades e ingresos"
   Buscar: "break even point formula calculation examples"
   Entender: costos fijos / (precio - costo variable) = unidades BE

SEMANA 3:

6. "Análisis de sensibilidad 3 escenarios"
   Buscar: "sensitivity analysis 3 scenarios pessimistic base optimistic"
   Entender: por qué un banco exige 3 escenarios
   Aplicar: el Excel tiene 3 columnas por indicador clave

7. "python-docx tabla landscape orientación horizontal"
   Buscar: "python-docx page orientation landscape section"
   Entender: el flujo de caja de 12 meses necesita orientación horizontal
```

### Skills a Crear en Este Sprint

```
.claude/skills/bpae-excel-maestro/SKILL.md
→ La estructura exacta del Excel maestro (hojas y propósito)
→ El principio del Panel de Control (solo ahí escribe el agente)
→ Cómo cargar la plantilla sin romper fórmulas
→ El mapeo: dato del plan_state → celda del Panel de Control
→ Cómo extraer indicadores del Excel una vez llenado
→ El problema data_only y cómo se resolvió

.claude/skills/bpae-coherence/SKILL.md
→ Qué verifica el Coherence Checker
→ Las reglas de negocio de validación financiera:
  - PE no puede superar el 90% de la capacidad instalada
  - TIR debe ser mayor a la tasa de descuento
  - Los ingresos proyectados no pueden superar el SOM
  - Payback máximo aceptable por sector
→ Cómo emitir alertas sin bloquear el avance
```

### Manipulación Word/Excel — Sprint 5

```
LA TAREA MÁS IMPORTANTE DEL SPRINT:
Diseñar la plantilla Excel maestra MANUALMENTE en Excel/LibreOffice
antes de escribir una línea de código que la manipule.

Ricardo abre Excel (no código) y diseña:
→ Hoja 0: Panel de Control con todos los inputs
→ Hoja 1-6: Hojas con fórmulas que solo referencian el Panel
→ Hoja 7: Gráficos automáticos

VERIFICACIÓN MANUAL:
→ Ricardo cambia el precio en el Panel
→ Todos los cálculos del Excel cambian automáticamente
→ El VAN y TIR recalculan sin tocar nada más
→ Solo cuando esto funciona perfecto, Ricardo escribe el código

SDD para llenar la plantilla:
/sdd:explore "servicio Python que llena el Panel de Control del Excel maestro"
→ El agente explica cómo leer datos del plan_state en Supabase
   y mapearlos a las celdas específicas del Panel de Control
→ Ricardo entiende el mapeo antes de aprobar
→ /sdd:new "excel-filler-service"
→ Spec, Design, Tasks → aprobados por Ricardo
→ /sdd:apply

TÉCNICA: Tablas financieras en Word
Buscar: "python-docx section landscape portrait mixed"
Entender: cómo mezclar páginas portrait y landscape en el mismo documento
Aplicar: el flujo de caja va en landscape, el resto del plan en portrait
```

### Entregable Verificable Sprint 5

```
CHECKLIST:
□ La plantilla Excel tiene todas las hojas y fórmulas correctas
□ Cambiar un input en el Panel recalcula todo automáticamente
□ El servicio llena el Panel sin tocar fórmulas
□ El Coherence Checker detecta al menos 3 tipos de inconsistencias
□ Las tablas financieras en Word son legibles y profesionales
□ El Excel generado abre correctamente en Excel y LibreOffice

CHECKLIST DE APRENDIZAJE:
□ Ricardo puede calcular el punto de equilibrio a mano con los datos de un plan
□ Ricardo puede interpretar el VAN y TIR de un plan de negocio
□ Ricardo tomó una decisión documentada sobre cómo leer valores calculados del Excel
□ Ricardo puede explicar por qué el agente solo escribe en el Panel de Control
```

---

## SPRINT 6: Compilación Final y Resumen Ejecutivo
### Duración: 2 semanas | El plan de negocio completo

```
OBJETIVO:
El compilador ensambla todas las secciones aprobadas en un Word final.
El Resumen Ejecutivo se genera con datos reales.
El usuario puede descargar el plan completo en Word y PDF.
```

### Conceptos a Investigar — Sprint 6

```
1. "python-docx combinar múltiples documentos"
   Buscar: "python-docx compose merge documents"
   Entender: cómo combinar Word parciales en uno final

2. "python-docx table of contents TOC"
   Buscar: "python-docx table of contents workaround"
   NOTA: python-docx no genera TOC automático.
   Ricardo investiga el workaround correcto.
   Hay al menos 2 soluciones distintas. Ricardo elige una y la documenta.

3. "Convertir Word a PDF en Python Linux"
   Buscar: "convert docx to pdf python linux libreoffice"
   Buscar: "docx2pdf python"
   Entender: opciones disponibles en Oracle Cloud (Linux)
   Aplicar: el sistema ofrece descarga en Word y PDF

4. "Streamlit download button"
   Buscar: "streamlit st.download_button tutorial"
   Aplicar: botones de descarga Word y PDF en la UI
```

### Skills a Crear en Este Sprint

```
.claude/skills/bpae-compiler/SKILL.md
→ El orden exacto de compilación de las secciones
→ Cómo insertar las tablas financieras del Excel en el Word
→ Cómo manejar secciones pendientes (placeholders)
→ Cómo generar el Resumen Ejecutivo desde los datos aprobados
→ El proceso de conversión a PDF

.claude/skills/bpae-word-plantilla/SKILL.md
→ La estructura de la plantilla Word base del proyecto
→ Los estilos de Nextstat: colores, tipografías, tamaños
→ Cómo aplicar los estilos del documento final
→ Convenciones de numeración, encabezados y pies de página
```

### Entregable Verificable Sprint 6

```
CHECKLIST:
□ El compilador ensambla todas las secciones en orden correcto
□ El Resumen Ejecutivo usa datos reales del plan (no inventados)
□ El índice del documento es correcto
□ El documento tiene numeración de páginas desde la página 2
□ Los estilos son consistentes en todo el documento
□ El PDF generado es de calidad profesional
□ El proceso completo de compilación tarda menos de 2 minutos

CHECKLIST DE APRENDIZAJE:
□ Ricardo puede explicar por qué el Resumen Ejecutivo va último pero se presenta primero
□ Ricardo documentó la solución al problema del TOC en engram
□ Ricardo puede regenerar el PDF si el cliente pide cambios menores
```

---

## SPRINT 7: Pulido, Tests y Primer Cliente Real
### Duración: 2 semanas | El MVP está listo para producción

```
OBJETIVO:
El sistema es confiable, está en producción en Oracle Cloud
y Ricardo lo usa con un cliente real de Nextstat.
```

### Conceptos a Investigar — Sprint 7

```
1. "pytest tutorial Python testing"
   Buscar: "pytest beginner guide fixtures assertions"
   Aplicar: tests para los servicios más críticos del sistema

2. "Python logging production best practices"
   Buscar: "python logging guide production"
   Aplicar: el sistema registra qué hace en cada paso

3. "FastAPI error handling middleware"
   Buscar: "FastAPI exception handler global"
   Aplicar: el sistema nunca muestra un error crudo al usuario

4. "Deploying FastAPI Oracle Cloud Ubuntu systemd"
   Buscar: "deploy FastAPI Ubuntu server systemd service"
   Aplicar: FastAPI y Streamlit corren 24/7 en Oracle Cloud

5. "Nginx reverse proxy Python application"
   Buscar: "nginx reverse proxy FastAPI Streamlit"
   Aplicar: acceso por URL pública sin exponer el puerto directamente
```

### Skills a Crear en Este Sprint

```
.claude/skills/bpae-deployment/SKILL.md
→ Cómo está configurado Oracle Cloud para este proyecto
→ Comandos para reiniciar los servicios
→ Cómo ver los logs de producción
→ El proceso de deploy de una nueva versión

.claude/skills/bpae-troubleshooting/SKILL.md
→ Los errores más comunes del sistema y sus soluciones
→ Cómo interpretar los logs de MiniMax cuando falla
→ Qué hacer si Supabase tiene problemas de conexión
→ Cómo recuperar un plan si el estado se corrompió
```

### La Prueba Final

```
Ricardo usa el sistema para hacer UN plan de negocio completo
con un cliente real de Nextstat.
Documenta en engram:
→ Qué funcionó exactamente como se planeó
→ Qué falló y cómo se resolvió en el momento
→ Qué le faltó al sistema que el cliente pidió
→ Cuánto tiempo tomó vs. el tiempo sin el sistema

Esta documentación define el backlog de la V2.
Si el tiempo se redujo a menos de la mitad: el MVP es un éxito.
```

---

## Resumen del Plan

```
FASE 0    Entorno + Fundamentos              1.5 semanas
SPRINT 1  Esqueleto + primeras skills        2 semanas
SPRINT 2  Motor de generación de texto       2 semanas
SPRINT 3  Agente Investigador                2 semanas
SPRINT 4  Investigación de mercado           3 semanas
SPRINT 5  Motor financiero Excel maestro     3 semanas
SPRINT 6  Compilación final                  2 semanas
SPRINT 7  Pulido + primer cliente real       2 semanas
──────────────────────────────────────────────────────
TOTAL:                                       17.5 semanas
```

---

## Hoja de Ruta de Skills SKILL.md del Proyecto

```
Fase 0:   bpae-context (contexto general del proyecto)
Sprint 1: bpae-fastapi, bpae-supabase
Sprint 2: bpae-prompts, bpae-generation
Sprint 3: bpae-investigador, bpae-pestel
Sprint 4: bpae-encuesta, bpae-mercado
Sprint 5: bpae-excel-maestro, bpae-coherence
Sprint 6: bpae-compiler, bpae-word-plantilla
Sprint 7: bpae-deployment, bpae-troubleshooting

AL FINAL DEL PROYECTO:
14 SKILL.md documentando exactamente cómo funciona cada módulo.
Un nuevo desarrollador puede entender el sistema completo
leyendo los skills y el engram del proyecto.
Eso es arquitectura sostenible.
```

---

*Plan de Implementación v2.0 — Nextstat 2026*
*Ricardo construye. La IA asiste con el Gentleman Stack. Ricardo aprende.*
