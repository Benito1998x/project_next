# ÍNDICE DE PLAN DE NEGOCIO - VERSIÓN MVP

> **Versión:** MVP (Producto Mínimo Viable)  
> **Propósito:** Estructura priorizada para desarrollo en 23 días  
> **Proyecto:** Business Plan Automation Engine (BPAE)  
> **Autor:** Ricardo Benito Vasquez Roca  
> **Deadline:** 23 días (Oracle Cloud Free Tier)

---

## Leyenda de Automatización

| Icono | Significado |
|-------|-------------|
| 🤖 | **Automatizable** - El agente puede generar con datos de entrada |
| 👤 | **Semi-automático** - Requiere input del usuario + generación |
| ✋ | **Manual** - El usuario debe proporcionar/procesar |
| ⚡ | **Prioridad Alta** - Sprint 1-3 |
| 🔸 | **Prioridad Media** - Sprint 4-5 |
| 🔹 | **Prioridad Baja** - Post-MVP |

---

## ESTRUCTURA MVP

```
PLAN DE NEGOCIO: [NOMBRE DEL PROYECTO]
```

---

## ⚡ PRELIMINARES

### ⚡ 0. Portada y Preliminares
- [ ] **0.1 Portada** 🤖⚡
  - Input: Nombre del negocio, logo, datos del emprendedor
  - Output: Portada profesional con identidad corporativa
  
- [ ] **0.2 Tabla de Contenido** 🤖⚡
  - Generada automáticamente desde la estructura del documento
  
- [ ] **0.3 Resumen Ejecutivo** 👤⚡
  - Input: Respuestas a 5 preguntas clave (Qué, Cómo, Con qué, Para qué, Cuánto)
  - Output: Síntesis de alto impacto generada por LLM

**Nota MVP:** Dedicatoria, agradecimientos y glosario se excluyen del MVP

---

## ⚡ CAPÍTULO I: DEFINICIÓN DEL NEGOCIO

**Objetivo:** *Establecer las bases conceptuales del negocio*

### ⚡ 1.1. Descripción del Negocio
- [ ] **1.1.1 Idea de Negocio** 🤖⚡
  - Input: Descripción breve del concepto (2-3 párrafos)
  - Output: Descripción formal del modelo de negocio
  
- [ ] **1.1.2 Misión y Visión** 🤖⚡
  - Input: Intenciones del emprendedor
  - Output: Misión y visión corporativas

### ⚡ 1.2. Análisis Inicial del Mercado
- [ ] **1.2.1 Identificación del Problema** 👤⚡
  - Input: ¿Qué problema resuelve el negocio?
  - Output: Descripción del problema y necesidad insatisfecha
  
- [ ] **1.2.2 Solución Propuesta** 🤖⚡
  - Input: Descripción de la solución
  - Output: Propuesta de valor inicial

**Secciones MVP excluidas:** Canvas completo, Value Proposition Canvas detallado

---

## ⚡ CAPÍTULO II: ANÁLISIS DE MERCADO

**Objetivo:** *Demostrar oportunidad de mercado mediante datos*

### ⚡ 2.1. Análisis del Entorno (PESTEL) 🤖⚡
- **Input:** Rubro, ciudad/país del negocio
- **Proceso:** 
  1. Agente Investigador busca datos en web (Tavily API)
  2. MiniMax 2.5 analiza y genera PESTEL
  3. Cache en Redis (24h)
- **Output:** Análisis PESTEL completo con fuentes

**Estructura:**
- [ ] 2.1.1 Político-Legal
- [ ] 2.1.2 Económico
- [ ] 2.1.3 Socio-Cultural
- [ ] 2.1.4 Tecnológico
- [ ] 2.1.5 Ecológico (opcional MVP)

### ⚡ 2.2. Análisis de Competencia (5 Fuerzas de Porter) 🤖⚡
- **Input:** Rubro, ubicación geográfica, competidores conocidos
- **Proceso:** Investigación web + síntesis con LLM
- **Output:** Análisis de las 5 fuerzas

**Estructura:**
- [ ] 2.2.1 Amenaza de nuevos entrantes
- [ ] 2.2.2 Poder de negociación de proveedores
- [ ] 2.2.3 Poder de negociación de clientes
- [ ] 2.2.4 Amenaza de sustitutos
- [ ] 2.2.5 Rivalidad del sector

### 🔸 2.3. Análisis FODA 🤖🔸
- **Input:** Datos de PESTEL y Porter
- **Output:** Fortalezas, Oportunidades, Debilidades, Amenazas

**MVP:** Matriz de estrategias post-MVP

---

## 🔸 CAPÍTULO III: INVESTIGACIÓN DE MERCADO

**Objetivo:** *Validar demanda con datos primarios*

### 🔸 3.1. Buyer Persona 👤🔸
- **Input:** Segmento objetivo deseado + datos de investigación
- **Output:** Perfil detallado del cliente ideal
- **Estado:** Semi-automático (requiere validación humana)

### 🔸 3.2. Diseño de Encuesta 👤🔸
- **Input:** Rubro, buyer persona
- **Proceso:**
  1. Agente genera instrumento de encuesta (10-15 preguntas)
  2. Usuario revisa y aprueba
  3. Sistema genera documento Word imprimible
  4. Usuario aplica encuesta manualmente (offline)
  5. Usuario sube resultados en Excel
  6. Sistema procesa con pandas y genera insights
- **Output:** Instrumento de encuesta profesional

### 🔸 3.3. Análisis de Demanda 🤖🔸
- [ ] **3.3.1 TAM/SAM/SOM** 🤖🔸
  - Input: Ubicación, rubro, datos de investigación
  - Output: Cálculo de mercado potencial, disponible y alcanzable
  
- [ ] **3.3.2 Proyección de Ventas** 👤🔸
  - Input: Capacidad instalada, precio estimado
  - Output: Proyección conservadora (3 años)
  - **Nota:** Requiere validación del usuario

---

## ⚡ CAPÍTULO IV: ANÁLISIS FINANCIERO

**Objetivo:** *Demostrar viabilidad económica*

### ⚡ 4.1. Inversiones Iniciales 👤⚡
- **Input:** Lista de activos necesarios con costos aproximados
- **Output:** Detalle de inversión fija y diferida
- **Secciones:**
  - [ ] 4.1.1 Inversión Fija (Equipos, mobiliario)
  - [ ] 4.1.2 Inversión Diferida (Constitución, estudios)
  - [ ] 4.1.3 Capital de Trabajo (Método simplificado)

### ⚡ 4.2. Estructura de Costos 👤⚡
- **Input:** Costos mensuales estimados
- **Output:** Clasificación de costos fijos y variables
- **Secciones:**
  - [ ] 4.2.1 Costos Fijos Mensuales
  - [ ] 4.2.2 Costos Variables (por unidad)

### ⚡ 4.3. Estado de Resultados Proyectado 🤖⚡
- **Input:** Proyección de ventas + estructura de costos
- **Proceso:** Plantilla Excel maestra con fórmulas
- **Output:** Estado de resultados (3 años)

### ⚡ 4.4. Flujo de Caja Proyectado 🤖⚡
- **Input:** Estado de resultados + inversiones
- **Output:** Flujo de caja mensual (Año 1), anual (Años 2-3)

### ⚡ 4.5. Indicadores de Rentabilidad 🤖⚡
- **Input:** Flujo de caja + supuestos financieros
- **Output:**
  - [ ] 4.5.1 VPN (Valor Presente Neto)
  - [ ] 4.5.2 TIR (Tasa Interna de Retorno)
  - [ ] 4.5.3 Punto de Equilibrio
  - [ ] 4.5.4 Payback (Período de recuperación)

### 🔸 4.6. Análisis de Sensibilidad 🔸
- **Post-MVP:** Escenarios optimista/base/pesimista

**MVP excluido:** WACC detallado, Balance General complejo, Análisis de riesgos profundo

---

## 🔹 CAPÍTULO V: CONCLUSIONES (POST-MVP)

**Objetivo:** *Síntesis final (Versión simplificada MVP)*

### 🔹 5.1. Síntesis de Viabilidad 🤖🔹
- Input: Resultados de todos los análisis
- Output: Párrafo conclusivo sobre viabilidad del negocio

### 🔹 5.2. Recomendaciones Clave 👤🔹
- Input: Hallazgos del plan
- Output: 3-5 recomendaciones prioritarias

**Versión completa:** Post-MVP (conclusiones detalladas por estudio)

---

## ANEXOS MVP

- **Anexo A:** Encuesta aplicada (instrumento generado)
- **Anexo B:** Resultados de encuesta (tabulación automática)
- **Anexo C:** Cotizaciones de equipos (input manual)
- **Anexo D:** Estados financieros en Excel (plantilla maestra)

**Anexos excluidos MVP:** Entrevistas, planos, mockups detallados, documentos legales completos

---

## ROADMAP DE IMPLEMENTACIÓN

### Sprint 1 (Semana 1): Esqueleto + Páginas Preliminares
- Portada automática
- Tabla de contenido dinámica
- Resumen ejecutivo básico
- Generación Sección 1 (Definición del Negocio)

### Sprint 2 (Semana 2): Motor de Generación
- Integración MiniMax 2.5
- Sistema de prompts estructurados
- Generación básica de texto

### Sprint 3 (Semana 3): Agente Investigador
- PESTEL automatizado
- Análisis Porter automatizado
- Cache con Redis

### Sprint 4 (Semanas 4-5): Investigación de Mercado
- Sistema de encuestas
- Procesamiento con pandas
- Cálculo TAM/SAM/SOM

### Sprint 5 (Semanas 6-7): Motor Financiero
- Plantilla Excel maestra
- Cálculo de indicadores (VPN, TIR, etc.)
- Exportación de tablas financieras

### Sprint 6 (Semana 8): Compilación Final
- Compilador de documentos Word
- Aplicación de estilos
- Descarga del plan completo

### Sprint 7 (Semana 9): Pulido y Deploy
- Tests básicos
- Deploy en Oracle Cloud
- Primer cliente real

---

## DECISIONES CLAVE DEL MVP

| Decisión | Justificación |
|----------|---------------|
| **Excluir Estudio Técnico detallado** | Complejidad alta, no crítico para MVP |
| **Excluir Estudio Organizacional completo** | Requiere mucho input manual |
| **Simplificar Marketing Digital** | Post-MVP con campañas reales |
| **Encuesta semi-automática** | Usuario aplica manual, sistema procesa |
| **Plantilla Excel con fórmulas** | Usuario revisa fórmulas, sistema solo llena inputs |
| **23 días Oracle** | Deadline real para forzar priorización |

---

## NOTAS PARA EL DESARROLLO

1. **Cada sección marcada con 🤖 debe tener:**
   - Prompt específico para MiniMax 2.5
   - Validación de output (JSON estructurado)
   - Fallback si el LLM falla

2. **Cada sección marcada con 👤 debe tener:**
   - Interfaz clara en Streamlit para input
   - Validación de datos antes de procesar
   - Preview antes de generar final

3. **Prioridad = Orden de desarrollo:**
   - ⚡ Sprint 1-3 (Must have)
   - 🔸 Sprint 4-5 (Should have)
   - 🔹 Sprint 6-7 (Nice to have)

---

*Documento de Trabajo - BPAE MVP*
