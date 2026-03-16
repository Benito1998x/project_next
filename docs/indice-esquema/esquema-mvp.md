# ESQUEMA DE BASE DE DATOS - MVP

> **Versión:** MVP (Producto Mínimo Viable)  
> **Proyecto:** Business Plan Automation Engine (BPAE)  
> **Enfoque:** Solo datos esenciales para los primeros 23 días  
> **Autor:** Ricardo Benito Vasquez Roca

---

## 🎯 PRINCIPIOS DEL ESQUEMA MVP

1. **Solo lo esencial** - Sin campos opcionales complejos
2. **JSON para secciones** - Campos flexibles en lugar de tablas separadas
3. **Foco en automatización** - Priorizar campos que el LLM puede generar
4. **Escalable** - Estructura que permite migrar a esquema completo después

---

## 📊 TABLAS PRINCIPALES MVP

### 1. tabla_usuarios
Usuarios del sistema (emprendedores)

```yaml
usuarios:
  id:
    tipo: uuid
    pk: true
  
  nombre_completo:
    tipo: string
    requerido: true
    ejemplo: "Ricardo Benito Vasquez Roca"
  
  email:
    tipo: string
    unique: true
    requerido: true
  
  nivel_academico:
    tipo: enum
    opciones: ["secundaria", "tecnico", "pregrado", "posgrado", "profesional"]
    default: "pregrado"
  
  contexto_destinatario:
    tipo: enum
    opciones: ["academico", "bancario", "inversionista", "personal"]
    default: "academico"
  
  created_at:
    tipo: datetime
    default: now()
```

---

### 2. tabla_planes (Principal)
Plan de negocio completo

```yaml
planes:
  # === IDENTIFICACIÓN ===
  id:
    tipo: uuid
    pk: true
  
  usuario_id:
    tipo: uuid
    fk: usuarios.id
  
  nombre_negocio:
    tipo: string
    requerido: true
    max: 200
    ejemplo: "Café Artesanal - La Paz"
  
  rubro:
    tipo: enum
    opciones: ["Gastronomía", "Tecnología", "Retail", "Servicios", "Manufactura", "Otro"]
    requerido: true
  
  ciudad:
    tipo: string
    requerido: true
    ejemplo: "La Paz"
  
  pais:
    tipo: string
    requerido: true
    default: "Bolivia"
  
  estado:
    tipo: enum
    opciones: ["borrador", "en_progreso", "completado"]
    default: "borrador"
  
  created_at:
    tipo: datetime
  
  updated_at:
    tipo: datetime
  
  # === CAP I: DEFINICIÓN DEL NEGOCIO ===
  cap1_definicion_negocio:
    tipo: json
    estructura:
      idea_negocio:              # text
      mision:                    # text (1-2 oraciones)
      vision:                    # text (1-2 oraciones)
      valores:                   # array[string] (3-5 items)
      problema_resuelve:         # text
      solucion_ofrecida:         # text
      diferenciador_clave:       # text
      canvas_9_modulos:          # object con 9 campos
        segmento_clientes: string
        propuesta_valor: string
        canales: string
        relacion_clientes: string
        fuentes_ingreso: string
        recursos_clave: string
        actividades_clave: string
        socios_clave: string
        estructura_costos: string
  
  # === CAP II: ANÁLISIS ENTORNO (Automatizado) ===
  cap2_analisis_entorno:
    tipo: json
    estructura:
      pestel:                    # object
        politico_legal: text
        economico: text
        socio_cultural: text
        tecnologico: text
        ecologico: text
        fuentes_tavily: array[string]  # URLs de investigación
      
      porter:                    # object
        amenaza_nuevos_entrantes: text + nivel
        poder_proveedores: text + nivel
        poder_clientes: text + nivel
        amenaza_sustitutos: text + nivel
        rivalidad_sector: text + nivel
      
      benchmarking:              # array de competidores (3-5)
        - nombre: string
          producto: string
          precio_aprox: decimal
          fortaleza: string
          debilidad: string
      
      foda:                      # object
        fortalezas: array[string]
        oportunidades: array[string]
        debilidades: array[string]
        amenazas: array[string]
      
      buyer_persona:             # object
        nombre_ficticio: string
        edad: integer
        ocupacion: string
        motivaciones: text
        frustraciones: text
        comportamiento_digital: text
  
  # === CAP III: INVESTIGACIÓN MERCADO ===
  cap3_investigacion_mercado:
    tipo: json
    estructura:
      encuesta_instrumento:      # text (contenido del Word)
      encuesta_resultados:       # array de respuestas (upload por usuario)
      encuesta_analisis:         # text generado automáticamente
      
      tam:                       # decimal (Total Addressable Market)
      sam:                       # decimal (Serviceable Available Market)
      som:                       # decimal (Serviceable Obtainable Market)
      
      proyeccion_ventas:         # array de 3 años
        year_1:
          unidades: integer
          ventas_total: decimal
        year_2:
          unidades: integer
          ventas_total: decimal
        year_3:
          unidades: integer
          ventas_total: decimal
  
  # === CAP VII: ANÁLISIS FINANCIERO (Prioridad Alta) ===
  cap7_analisis_financiero:
    tipo: json
    estructura:
      inversiones_iniciales:
        inversion_fija: decimal
        inversion_diferida: decimal
        capital_trabajo: decimal
      
      estructura_costos:
        costo_unitario_mp: decimal      # Materia prima por unidad
        costos_fijos_mensuales: decimal
        gastos_operativos: decimal
      
      estados_financieros:
        estado_resultados: array[3]      # Uno por año
        flujo_caja: array[3]
      
      indicadores_rentabilidad:
        punto_equilibrio_unidades: integer
        vpn: decimal
        tir: decimal
        payback_meses: integer
  
  # === RESUMEN EJECUTIVO ===
  resumen_ejecutivo:
    tipo: json
    estructura:
      que: text
      como: text
      con_que: text
      para_que: text
      cuanto: decimal
      roi_esperado: decimal
  
  # === METADATOS ===
  metadata:
    tipo: json
    estructura:
      progreso_porcentaje: integer      # 0-100
      capitulos_completados: array[string]
      ultima_seccion_trabajada: string
      version_plan: string              # "1.0"
```

---

### 3. tabla_secciones_generadas (Log)
Registro de contenido generado por el LLM

```yaml
secciones_generadas:
  id:
    tipo: uuid
    pk: true
  
  plan_id:
    tipo: uuid
    fk: planes.id
  
  capitulo:
    tipo: enum
    opciones: ["cap1", "cap2", "cap3", "cap7"]
  
  subcapitulo:
    tipo: string
    ejemplo: "pestel", "porter", "canvas"
  
  prompt_utilizado:
    tipo: text
    descripcion: "El prompt completo enviado al LLM"
  
  respuesta_raw:
    tipo: text
    descripcion: "Respuesta cruda del LLM antes de procesar"
  
  contenido_procesado:
    tipo: text
    descripcion: "Contenido final guardado en el plan"
  
  fuentes_utilizadas:
    tipo: array[string]
    descripcion: "URLs de Tavily usadas"
  
  estado:
    tipo: enum
    opciones: ["generando", "completado", "error", "reintentando"]
    default: "generando"
  
  tokens_usados:
    tipo: integer
    descripcion: "Tokens consumidos en la llamada"
  
  tiempo_generacion_segundos:
    tipo: integer
  
  created_at:
    tipo: datetime
```

---

### 4. tabla_cache_investigacion (Optimización)
Cache de investigaciones Tavily para no repetir búsquedas

```yaml
cache_investigacion:
  id:
    tipo: uuid
    pk: true
  
  query_hash:
    tipo: string
    unique: true
    descripcion: "Hash de la consulta (rubro + ciudad + tema)"
  
  query_original:
    tipo: string
    ejemplo: "café sector Bolivia economía regulaciones"
  
  resultados:
    tipo: json
    descripcion: "Respuesta completa de Tavily"
  
  fecha_consulta:
    tipo: datetime
  
  expires_at:
    tipo: datetime
    default: "fecha_consulta + 24 horas"
    descripcion: "TTL de 24 horas"
```

---

## 🔗 RELACIONES ENTRE TABLAS (MVP)

```
┌─────────────────────────────────────────────────────────┐
│                    usuarios                             │
│  (id, nombre, email, nivel_academico)                  │
└────────────┬────────────────────────────────────────────┘
             │
             │ 1:N
             ▼
┌─────────────────────────────────────────────────────────┐
│                    planes                               │
│  (id, usuario_id, nombre_negocio, rubro, ciudad)       │
│  + campos JSON: cap1_definicion_negocio                │
│                 cap2_analisis_entorno                  │
│                 cap3_investigacion_mercado             │
│                 cap7_analisis_financiero               │
│                 resumen_ejecutivo                      │
└────────────┬────────────────────────────────────────────┘
             │
             │ 1:N
             ▼
┌─────────────────────────────────────────────────────────┐
│              secciones_generadas                        │
│  (id, plan_id, capitulo, subcapitulo, contenido)       │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│              cache_investigacion                        │
│  (query_hash, resultados, expires_at)                  │
│  (Tabla independiente, usada por todos)                │
└─────────────────────────────────────────────────────────┘
```

---

## 📋 EJEMPLO DE INSERCIÓN

```json
{
  "tabla": "planes",
  "datos": {
    "id": "550e8400-e29b-41d4-a716",
    "usuario_id": "user-123",
    "nombre_negocio": "Café Artesanal - La Paz",
    "rubro": "Gastronomía",
    "ciudad": "La Paz",
    "pais": "Bolivia",
    "cap1_definicion_negocio": {
      "idea_negocio": "Cafetería especializada en café de origen boliviano...",
      "mision": "Ofrecer café de especialidad de origen boliviano...",
      "vision": "Ser la cadena de cafeterías líder en Bolivia...",
      "valores": ["Calidad", "Sostenibilidad", "Comunidad"],
      "problema_resuelve": "Falta de espacios con café de calidad y ambiente profesional",
      "solucion_ofrecida": "Café de especialidad en ambiente acogedor",
      "diferenciador_clave": "100% café boliviano de pequeños productores",
      "canvas_9_modulos": {
        "segmento_clientes": "Jóvenes profesionales 25-40 años",
        "propuesta_valor": "Café de especialidad de origen boliviano",
        "canales": "Local físico + delivery",
        "relacion_clientes": "Atención personalizada y programa de fidelización",
        "fuentes_ingreso": "Venta de café y alimentos",
        "recursos_clave": "Baristas capacitados, equipos de calidad",
        "actividades_clave": "Preparación de café, atención al cliente",
        "socios_clave": "Cooperativas de productores, proveedores de lácteos",
        "estructura_costos": "Costos fijos: alquiler, sueldos. Variables: materia prima"
      }
    },
    "cap2_analisis_entorno": {
      "pestel": {
        "politico_legal": "Estabilidad política media. Regulaciones sanitarias...",
        "economico": "PIB creciendo 3.5%, inflación controlada...",
        "socio_cultural": "Tendencia consumo café especialidad creciente...",
        "tecnologico": "Apps delivery ampliamente adoptadas...",
        "ecologico": "Mayor conciencia sostenibilidad..."
      },
      "porter": {
        "amenaza_nuevos_entrantes": { "analisis": "Barreras medias...", "nivel": "media" },
        "poder_proveedores": { "analisis": "Muchos proveedores disponibles...", "nivel": "bajo" },
        "poder_clientes": { "analisis": "Alto, muchas opciones disponibles...", "nivel": "alto" },
        "amenaza_sustitutos": { "analisis": "Té, bebidas energéticas...", "nivel": "media" },
        "rivalidad_sector": { "analisis": "Alta, varias cadenas establecidas...", "nivel": "alta" }
      },
      "foda": {
        "fortalezas": ["Producto diferenciado", "Precio competitivo"],
        "oportunidades": ["Tendencia café especialidad", "Turismo creciente"],
        "debilidades": ["Marca desconocida", "Capital limitado"],
        "amenazas": ["Competencia establecida", "Crisis económica"]
      },
      "buyer_persona": {
        "nombre_ficticio": "María, la ejecutiva",
        "edad": 32,
        "ocupacion": "Ejecutiva de marketing",
        "motivaciones": "Calidad, ambiente para reuniones de trabajo",
        "frustraciones": "Cafés ruidosos, mala atención",
        "comportamiento_digital": "Instagram daily, pide delivery 2x semana"
      }
    }
  }
}
```

---

## ⚡ DIFERENCIAS: MVP vs COMPLETO

| Aspecto | MVP (Este archivo) | Completo |
|---------|-------------------|----------|
| **Capítulos** | Solo I, II, III, VII | I, II, III, IV, V, VI, VII, VIII |
| **Tablas** | 4 tablas | 10+ tablas normalizadas |
| **Estructura** | JSON flexible | Tablas relacionadas 1:N |
| **Campos** | Esenciales solo | Todos los campos detallados |
| **Encuestas** | Resultados en JSON | Tabla separada con análisis |
| **Competidores** | Array en JSON | Tabla separada con relaciones |
| **Finanzas** | JSON básico | Tablas: inversiones, costos, estados |
| **Usuarios** | Básico | Con roles, permisos, equipos |

---

## 🎯 PRÓXIMOS PASOS CON ESTE ESQUEMA

1. **Crear tabla `planes`** en Supabase con campos JSON
2. **Implementar endpoint** POST /planes (guardar datos básicos)
3. **Implementar endpoint** GET /planes/{id}/cap1 (recuperar definición)
4. **Implementar generación** automática con LLM para cap2
5. **Migrar a esquema completo** después del MVP (día 23+)

---

*Esquema MVP - BPAE v1.0*
