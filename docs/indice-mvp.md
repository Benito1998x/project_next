# ÍNDICE DE PLAN DE NEGOCIO - VERSIÓN MVP

> **Versión:** MVP (Producto Mínimo Viable)
> **Propósito:** Estructura priorizada para desarrollo automatizado en 23 días
> **Proyecto:** Business Plan Automation Engine (BPAE)
> **Autor:** Ricardo Benito Vasquez Roca
> **Deadline:** 23 días (Oracle Cloud Free Tier)

---

## Leyenda de Automatización

| Icono | Significado |
|-------|-------------|
| 🤖 | **Automatizable** — El agente genera con datos de entrada |
| 👤 | **Semi-automático** — Requiere input del usuario + generación |
| ✋ | **Manual** — El usuario debe proporcionar/procesar directamente |
| ⚡ | **Prioridad Alta** — Sprint 1-4 (Must Have) |
| 🔸 | **Prioridad Media** — Sprint 5-6 (Should Have) |
| 🔹 | **Prioridad Baja** — Post-MVP (Nice to Have) |

---

## ESTRUCTURA MVP

```
PLAN DE NEGOCIO: [NOMBRE DEL PROYECTO]
```

---

## ⚡ PRELIMINARES

### ⚡ 0. Portada y Páginas Iniciales
- [ ] **0.1 Portada** 🤖⚡
  - Input: Nombre del negocio, logo, datos del emprendedor
  - Output: Portada profesional con identidad corporativa

- [ ] **0.2 Tabla de Contenido** 🤖⚡
  - Generada automáticamente desde la estructura del documento

- [ ] **0.3 Resumen Ejecutivo** 👤⚡
  - Input: Respuestas a 5 preguntas clave (¿Qué?, ¿Cómo?, ¿Con qué?, ¿Para qué?, ¿Cuánto?)
  - Output: Síntesis de alto impacto generada por LLM (máx. 1 página)

**Nota MVP:** Dedicatoria, agradecimientos y glosario se excluyen del MVP

---

## ⚡ CAPÍTULO I: DEFINICIÓN DEL NEGOCIO

**Objetivo:** *Establecer las bases conceptuales y la propuesta de valor del negocio*

### ⚡ 1.1. Descripción del Negocio
- [ ] **1.1.1 Idea de Negocio** 🤖⚡
  - Input: Descripción breve del concepto (2-3 párrafos del emprendedor)
  - Output: Descripción formal y estructurada del modelo de negocio

- [ ] **1.1.2 Misión y Visión** 🤖⚡
  - Input: Propósito, valores e intenciones del emprendedor
  - Output: Misión y visión corporativas redactadas profesionalmente

- [ ] **1.1.3 Propuesta de Valor** 🤖⚡
  - Input: Problema que resuelve + beneficio diferencial frente a la competencia
  - Output: Propuesta de valor única (formato Value Proposition simplificado)

### ⚡ 1.2. Modelo de Negocio Canvas (Simplificado)
- [ ] **1.2.1 Canvas de 9 Módulos** 🤖⚡
  - Input: Respuestas del emprendedor a los 9 módulos del CANVAS
  - Output: Lienzo de modelo de negocio resumido (versión 1 página)
  - Módulos: Segmento, Propuesta de Valor, Canales, Relación con Clientes, Fuentes de Ingreso, Recursos Clave, Actividades Clave, Socios Clave, Estructura de Costos

**Secciones MVP excluidas:** Value Proposition Canvas detallado, Cadena de Valor completa

---

## ⚡ CAPÍTULO II: ANÁLISIS DEL ENTORNO Y MERCADO

**Objetivo:** *Demostrar oportunidad de mercado y definir con precisión a quién sirve el negocio*

### ⚡ 2.1. Análisis del Entorno (PESTEL) 🤖⚡
- **Input:** Rubro, ciudad/país del negocio
- **Proceso:**
  1. Agente Investigador busca datos en web (Tavily API)
  2. LLM analiza y genera PESTEL con fuentes
  3. Cache en Redis (24h TTL)
- **Output:** Análisis PESTEL completo con fuentes citadas

**Estructura:**
- [ ] 2.1.1 Político-Legal
- [ ] 2.1.2 Económico
- [ ] 2.1.3 Socio-Cultural
- [ ] 2.1.4 Tecnológico
- [ ] 2.1.5 Ecológico (opcional MVP)

### ⚡ 2.2. Análisis de Competencia (5 Fuerzas de Porter + Benchmarking) 🤖⚡
- **Input:** Rubro, ubicación geográfica, competidores conocidos
- **Proceso:** Investigación web + síntesis con LLM
- **Output:** Análisis de las 5 fuerzas + tabla comparativa de competidores

**Estructura:**
- [ ] 2.2.1 Amenaza de nuevos entrantes
- [ ] 2.2.2 Poder de negociación de proveedores
- [ ] 2.2.3 Poder de negociación de clientes
- [ ] 2.2.4 Amenaza de sustitutos
- [ ] 2.2.5 Rivalidad del sector
- [ ] 2.2.6 Benchmarking de Competidores Clave 🤖
  - Tabla: Competidor, Producto/Servicio, Precio, Canal, Fortaleza, Debilidad

### 🔸 2.3. Análisis FODA 🤖🔸
- **Input:** Datos de PESTEL y Porter + información del negocio
- **Output:** Fortalezas, Oportunidades, Debilidades, Amenazas

**MVP:** Matriz de estrategias FO/DO/FA/DA post-MVP

### ⚡ 2.4. Buyer Persona y Customer Journey 👤⚡
- **Input:** Segmento objetivo + hallazgos de PESTEL y Porter
- **Output:** Perfil del cliente ideal + mapa de experiencia simplificado
- **Secciones:**
  - [ ] 2.4.1 Ficha del Buyer Persona 👤
    - Nombre ficticio, edad, ocupación, nivel socioeconómico
    - Motivaciones, frustraciones y objetivos (Pain & Gain)
    - Comportamiento digital y criterios de decisión de compra
  - [ ] 2.4.2 Customer Journey Simplificado 🤖
    - Etapas: Descubrimiento → Evaluación → Compra → Fidelización
    - Touchpoints principales y emociones clave por etapa

**Nota:** El Buyer Persona generado aquí alimenta el Plan de Marketing (Cap. V)

---

## 🔸 CAPÍTULO III: INVESTIGACIÓN DE MERCADO

**Objetivo:** *Validar la demanda con datos primarios y cuantificar el mercado*

### 🔸 3.1. Diseño y Aplicación de Encuesta 👤🔸
- **Input:** Rubro, buyer persona (desde 2.4)
- **Proceso:**
  1. Agente genera instrumento (10-15 preguntas validadas)
  2. Usuario revisa y aprueba el instrumento
  3. Sistema genera documento Word imprimible
  4. Usuario aplica la encuesta manualmente (campo)
  5. Usuario sube resultados en Excel
  6. Sistema procesa con pandas y genera análisis visual
- **Output:** Instrumento de encuesta profesional + informe de resultados con gráficos

### 🔸 3.2. Análisis de Demanda 🤖🔸
- [ ] **3.2.1 TAM / SAM / SOM** 🤖🔸
  - Input: Ubicación, rubro, datos de investigación y encuesta
  - Output: Cálculo de mercado potencial, disponible y alcanzable con metodología

- [ ] **3.2.2 Proyección de Ventas** 👤🔸
  - Input: Capacidad instalada estimada, precio de venta
  - Output: Proyección conservadora de ventas (3 años, con supuestos explícitos)
  - **Nota:** Requiere validación y aprobación del usuario

---

## ⚡ CAPÍTULO IV: ASPECTOS TÉCNICOS ESENCIALES

**Objetivo:** *Demostrar viabilidad operativa y proveer los datos técnicos que sustentan los costos financieros*

### ⚡ 4.1. Ficha Técnica del Producto/Servicio 👤⚡
- **Input:** Descripción técnica del producto o servicio
- **Output:** Ficha técnica estructurada
- **Secciones:**
  - [ ] 4.1.1 Especificaciones Técnicas, Ingredientes o Componentes ✋
  - [ ] 4.1.2 Diagrama de Flujo del Proceso (simplificado) 👤
  - [ ] 4.1.3 Capacidad de Producción / Prestación Estimada 👤

### ⚡ 4.2. Proveedores y Materiales 👤⚡
- **Input:** Lista de materiales/insumos y proveedores conocidos
- **Proceso:** Usuario ingresa datos; sistema calcula costos unitarios
- **Output:** Cuadro de proveedores e insumos con costos
- **Secciones:**
  - [ ] 4.2.1 BOM Simplificado (Lista de Materiales e Insumos) ✋
    - Descripción, unidad de medida, cantidad por unidad producida
  - [ ] 4.2.2 Cuadro de Proveedores Clave 👤
    - Nombre del proveedor, producto que provee, precio referencial, condiciones de pago
  - [ ] 4.2.3 Costo Unitario de Materia Prima 🤖
    - Cálculo automático: BOM × precios de proveedores

**Nota:** El costo unitario (4.2.3) alimenta directamente la Estructura de Costos (Cap. VII.7.3)

### 🔸 4.3. Inocuidad y Calidad Básica 🤖🔸
- **Input:** Tipo de producto/servicio, rubro
- **Output:** Lista de requisitos sanitarios mínimos y puntos de control críticos
- **Secciones:**
  - [ ] 4.3.1 Requisitos Sanitarios y Permisos Necesarios 🤖
    - Registro sanitario, licencia municipal, habilitaciones del sector
  - [ ] 4.3.2 Puntos Críticos de Control Simplificados (HACCP básico) 👤
    - Solo para negocios de alimentos; identifica los 3-5 PCC más importantes

**MVP excluido:** Distribución de planta detallada, plan de mantenimiento, HACCP completo con árbol de decisiones

---

## 🔸 CAPÍTULO V: PLAN DE MARKETING BÁSICO

**Objetivo:** *Definir cómo se captará al cliente, se generarán ventas y se construirá la marca*

### 🔸 5.1. Estrategia de Posicionamiento y Precio 🤖🔸
- **Input:** Datos del producto, buyer persona (2.4), benchmarking de competidores (2.2.6)
- **Output:** Posicionamiento diferenciado y estrategia de precios justificada
- **Secciones:**
  - [ ] 5.1.1 Posicionamiento y Diferenciación 🤖
    - Declaración de posicionamiento (para quién, qué ofrece, por qué es diferente)
  - [ ] 5.1.2 Estrategia de Precios 👤
    - Método de fijación (costo+margen / valor percibido / comparativo)
    - Precio de venta recomendado con justificación

### 🔸 5.2. Canales, Comunicación y Presupuesto 👤🔸
- **Input:** Buyer persona, canales disponibles, presupuesto estimado
- **Output:** Plan de canales y comunicación accionable
- **Secciones:**
  - [ ] 5.2.1 Canales de Venta (online y offline) 👤
  - [ ] 5.2.2 Mensajes Clave por Etapa del Customer Journey 🤖
    - Etapa Descubrimiento / Evaluación / Decisión / Fidelización
  - [ ] 5.2.3 Presencia Digital Básica 🤖
    - Plataformas recomendadas, frecuencia de publicación, tipo de contenido por red
  - [ ] 5.2.4 Presupuesto de Marketing Inicial (Mes 1-3) 👤
    - Distribución de inversión: orgánico vs. pagado

**MVP excluido:** Plan detallado de campañas Meta Ads, calendario editorial, mockups de anuncios, estrategia de puja

---

## ⚡ CAPÍTULO VI: ESTRUCTURA ORGANIZACIONAL BÁSICA

**Objetivo:** *Establecer la forma legal y el equipo mínimo para operar el negocio*

### ⚡ 6.1. Constitución Legal 🤖⚡
- **Input:** País/ciudad, tipo de negocio, socios (si aplica)
- **Proceso:** Agente investiga opciones legales locales + genera recomendación
- **Output:** Tipo societario recomendado + pasos de constitución + costos estimados
- **Secciones:**
  - [ ] 6.1.1 Tipo de Sociedad Recomendado y Justificación 🤖
  - [ ] 6.1.2 Pasos para la Constitución y Costos Estimados 🤖
  - [ ] 6.1.3 Obligaciones Tributarias Clave (Régimen fiscal recomendado) 🤖

### ⚡ 6.2. Equipo y Organización 👤⚡
- **Input:** Fundadores, roles disponibles, contrataciones planificadas
- **Output:** Organigrama simplificado + descripción de puestos clave
- **Secciones:**
  - [ ] 6.2.1 Organigrama Inicial 🤖
  - [ ] 6.2.2 Perfiles y Funciones Clave ✋
    - Cargo, responsabilidades principales, costo mensual (alimenta Cap. VII.7.3)
  - [ ] 6.2.3 Plan de Contratación (Mes de inicio por cargo) 👤

**MVP excluido:** Manual de funciones completo, políticas de RRHH detalladas, evaluación del desempeño, alianzas estratégicas

---

## ⚡ CAPÍTULO VII: ANÁLISIS FINANCIERO

**Objetivo:** *Demostrar la viabilidad económica con datos reales del negocio*

### ⚡ 7.1. Supuestos Macroeconómicos y Financieros 🤖⚡
- **Input:** País/ciudad del negocio, sector económico
- **Proceso:** Agente busca datos macro oficiales (banco central u organismo equivalente)
- **Output:** Tabla de supuestos base que sustenta todas las proyecciones
- **Secciones:**
  - [ ] 7.1.1 Inflación, Devaluación y Tasas de Interés Proyectadas 🤖
  - [ ] 7.1.2 Horizonte de Evaluación 👤 (default: 3 años para MVP)
  - [ ] 7.1.3 Tasa de Impuesto a la Renta (según régimen tributario) ✋

### ⚡ 7.2. Inversiones Iniciales 👤⚡
- **Input:** Lista de activos necesarios con costos aproximados
- **Output:** Detalle de inversión fija, diferida y capital de trabajo
- **Secciones:**
  - [ ] 7.2.1 Inversión Fija (Equipos, mobiliario, infraestructura)
  - [ ] 7.2.2 Inversión Diferida (Constitución, estudios, licencias — desde Cap. VI)
  - [ ] 7.2.3 Capital de Trabajo (Método simplificado: ciclo operativo promedio)

### ⚡ 7.3. Estructura de Costos 👤⚡
- **Input:** BOM/Proveedores (IV.4.2) + Equipo (VI.6.2) + costos operativos estimados
- **Output:** Clasificación completa de costos fijos y variables
- **Secciones:**
  - [ ] 7.3.1 Costo de Ventas
    - Materia Prima (desde BOM × proyección de ventas)
    - Mano de Obra Directa
    - Costos Indirectos de Fabricación (CIF)
  - [ ] 7.3.2 Gastos Operativos Fijos Mensuales
    - Administrativos, ventas, marketing (desde Cap. V)
  - [ ] 7.3.3 Depreciación (método lineal simplificado)

### ⚡ 7.4. Estados Financieros Proyectados 🤖⚡
- **Input:** Proyección de ventas (III.3.2) + estructura de costos (7.3) + supuestos (7.1)
- **Proceso:** Plantilla Excel maestra con fórmulas precargadas
- **Output:** Los 3 estados financieros esenciales
- **Secciones:**
  - [ ] 7.4.1 Estado de Resultados (P&L) Proyectado — 3 años
  - [ ] 7.4.2 Flujo de Caja Proyectado
    - Mensual (Año 1) + Anual (Años 2-3)
  - [ ] 7.4.3 Balance General Proyectado (simplificado)

### ⚡ 7.5. Indicadores de Rentabilidad 🤖⚡
- **Input:** Flujo de caja + supuestos financieros (7.1)
- **Output:** Dashboard de viabilidad financiera
- **Secciones:**
  - [ ] 7.5.1 Punto de Equilibrio (unidades y valor monetario)
  - [ ] 7.5.2 VPN (Valor Presente Neto)
  - [ ] 7.5.3 TIR (Tasa Interna de Retorno)
  - [ ] 7.5.4 Payback (Período de recuperación simple)

### 🔸 7.6. Análisis de Sensibilidad 🔸
- **Input:** Variables críticas identificadas en el negocio
- **Output:** Escenarios optimista / base / pesimista
- **Post-MVP:** Análisis de sensibilidad cruzada y simulación Monte Carlo

**MVP excluido:** WACC/TMAR detallado, Payback descontado, análisis de riesgos financieros profundo

---

## 🔹 CAPÍTULO VIII: CONCLUSIONES

**Objetivo:** *Síntesis final y veredicto de viabilidad integral*

### 🔹 8.1. Síntesis de Viabilidad 🤖🔹
- Input: Resultados de todos los capítulos
- Output: Párrafo conclusivo integrado sobre la viabilidad del negocio

### 🔹 8.2. Recomendaciones Clave 👤🔹
- Input: Hallazgos más relevantes del plan
- Output: 3-5 recomendaciones prioritarias para la puesta en marcha

**Versión completa:** Conclusiones detalladas por capítulo con veredicto formal

---

## ANEXOS MVP

- **Anexo A:** Instrumento de Encuesta (generado automáticamente)
- **Anexo B:** Tabulación de Resultados de Encuesta (procesado automáticamente)
- **Anexo C:** Cotizaciones de Equipos y Proveedores (input manual del usuario)
- **Anexo D:** Plantilla Excel de Estados Financieros (modelo maestra con fórmulas)

**Anexos excluidos MVP:** Transcripción de entrevistas, planos, mockups de campañas, certificaciones completas

---

## FLUJO DE DATOS ENTRE CAPÍTULOS

```
II.2.4  Buyer Persona         ──►  V   Plan de Marketing
II.2.2  Benchmarking          ──►  V   Estrategia de Precios
III.3.2 Proyección de Ventas  ──►  VII.7.4 Estados Financieros
IV.4.2  BOM / Proveedores     ──►  VII.7.3 Estructura de Costos
VI.6.2  Equipo / Nómina       ──►  VII.7.3 Costos de RRHH
VI.6.1  Constitución Legal    ──►  VII.7.2 Inversión Diferida
VII.7.1 Supuestos Macro       ──►  VII.7.4 y VII.7.5
```

---

## ROADMAP DE IMPLEMENTACIÓN

### Sprint 1 (Semana 1): Esqueleto + Capítulo I y II.2.1
- Portada automática y tabla de contenido dinámica
- Resumen ejecutivo básico
- Generación Cap. I (Definición del Negocio + Canvas simplificado)
- PESTEL automatizado (Cap. II.2.1)

### Sprint 2 (Semana 2): Análisis de Mercado Completo
- Porter + Benchmarking automatizado (Cap. II.2.2)
- FODA automatizado (Cap. II.2.3)
- Buyer Persona + Customer Journey (Cap. II.2.4)

### Sprint 3 (Semana 3): Investigación de Mercado
- Sistema de encuestas (instrumento + generación Word)
- Procesamiento de resultados con pandas
- Cálculo TAM/SAM/SOM y proyección de ventas (Cap. III)

### Sprint 4 (Semana 4): Aspectos Técnicos y Marketing
- Ficha técnica y diagrama de proceso (Cap. IV.4.1)
- BOM y cuadro de proveedores con cálculo de costos (Cap. IV.4.2)
- Plan de Marketing básico (Cap. V)

### Sprint 5 (Semana 5): Organización y Base Financiera
- Constitución legal e investigación de tipo societario (Cap. VI.6.1)
- Organigrama y equipo clave (Cap. VI.6.2)
- Supuestos macro + inversiones + estructura de costos (Cap. VII.7.1–7.3)

### Sprint 6 (Semana 6): Motor Financiero
- Plantilla Excel maestra con fórmulas
- Los 3 estados financieros proyectados (Cap. VII.7.4)
- Dashboard de indicadores de rentabilidad (Cap. VII.7.5)

### Sprint 7 (Semana 7): Conclusiones, Compilación y Deploy
- Conclusiones y recomendaciones automáticas (Cap. VIII)
- Compilador de documento Word completo con estilos
- Tests básicos de integración
- Deploy en Oracle Cloud + prueba con primer cliente real

---

## DECISIONES CLAVE DEL MVP

| Decisión | Justificación |
|----------|---------------|
| **Estudio Técnico simplificado** | Solo ficha técnica, proceso y proveedores; distribución de planta, HACCP completo y plan de mantenimiento son post-MVP |
| **Marketing básico incluido (Cap. V)** | Sin estrategia de marketing el plan queda incompleto e inviable; las 4P mínimas son irrenunciables |
| **Organización básica incluida (Cap. VI)** | La constitución legal y el equipo impactan directamente los costos y la inversión diferida |
| **3 estados financieros** | P&L + Flujo de Caja + Balance son mínimos irrenunciables para evaluar viabilidad |
| **Buyer Persona en Cap. II** | Al generarse tras PESTEL y Porter, tiene base de datos real y alimenta todo el plan |
| **Encuesta semi-automática** | Usuario aplica en campo; sistema procesa y genera análisis automáticamente |
| **Plantilla Excel con fórmulas** | Usuario revisa fórmulas; sistema solo llena inputs desde los datos del plan |
| **23 días Oracle** | Deadline real que fuerza priorización estricta y evita feature creep |

---

## NOTAS PARA EL DESARROLLO

1. **Cada sección 🤖 debe tener:**
   - Prompt específico para el LLM (versionado en `/prompts/`)
   - Esquema de validación del output (JSON estructurado con Pydantic)
   - Fallback si el LLM falla o retorna respuesta incompleta

2. **Cada sección 👤 debe tener:**
   - Formulario claro en Streamlit con validación de campos
   - Vista previa del contenido antes de confirmar
   - Opción de regenerar con LLM si el usuario no está satisfecho

3. **Prioridad = Orden de desarrollo:**
   - ⚡ Sprint 1-4 (Must Have — bloquea el resto si falta)
   - 🔸 Sprint 5-6 (Should Have — completa el plan para ser profesional)
   - 🔹 Sprint 7 (Nice to Have — agrega valor pero no bloquea el MVP)

---

*Documento de Trabajo - BPAE MVP*
