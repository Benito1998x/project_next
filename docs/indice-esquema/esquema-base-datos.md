# ESQUEMA DE BASE DE DATOS - BPAE

> **Proyecto:** Business Plan Automation Engine  
> **Tipo:** Esquema de datos por sección del Plan de Negocio  
> **Estructura:** Campos, tipos, validaciones y contexto  
> **Autor:** Ricardo Benito Vasquez Roca

---

## 🎭 CONTEXTO DEL TONO

Antes de diseñar la base de datos, el sistema debe conocer el **nivel de formalidad** del plan:

```json
{
  "tono_proyecto": {
    "nivel_academico": "enum[secundaria, pregrado, posgrado, profesional, doctorado]",
    "contexto_destinatario": "enum[academico, bancario, inversionista, personal, concurso]",
    "complejidad": "enum[simple, estandar, complejo, muy_complejo]",
    "sector_industrial": "string",
    "pais_region": "string"
  }
}
```

**Ejemplos de Tono:**
- `nivel_academico: "secundaria"` → Lenguaje simple, explicaciones básicas
- `nivel_academico: "posgrado"` → Marco teórico, citas bibliográficas
- `contexto_destinatario: "bancario"` → Enfoque en viabilidad financiera y garantías
- `contexto_destinatario: "inversionista"` → ROI, escalabilidad, salida (exit strategy)

---

## 📋 ESQUEMAS POR SECCIÓN

---

### 0. PRELIMINARES

#### 0.1 PORTADA

```yaml
portada:
  nombre_negocio:
    tipo: string
    requerido: true
    min: 3
    max: 200
    descripcion: "Nombre comercial del proyecto"
    ejemplo: "Café Artesanal - La Paz"
  
  slogan_subtitulo:
    tipo: string
    requerido: false
    max: 150
    descripcion: "Eslogan o descripción corta del negocio"
    ejemplo: "El auténtico sabor de Bolivia en cada taza"
  
  nombre_emprendedor:
    tipo: string
    requerido: true
    max: 100
    descripcion: "Nombre completo del emprendedor o razón social"
  
  cargo_posicion:
    tipo: string
    requerido: false
    default: "Emprendedor"
    descripcion: "Cargo o posición en la empresa"
    opciones: ["CEO", "Fundador", "Emprendedor", "Gerente General"]
  
  email_contacto:
    tipo: email
    requerido: true
    descripcion: "Email de contacto principal"
  
  telefono_contacto:
    tipo: string
    requerido: false
    descripcion: "Teléfono de contacto"
  
  institucion_evaluadora:
    tipo: string
    requerido: false
    descripcion: "Universidad, banco o institución ante quien se presenta el plan"
  
  ciudad:
    tipo: string
    requerido: true
    descripcion: "Ciudad de operación"
  
  pais:
    tipo: string
    requerido: true
    descripcion: "País de operación"
  
  fecha_elaboracion:
    tipo: date
    requerido: true
    default: "current_date"
    descripcion: "Fecha de elaboración del plan"
  
  logo_url:
    tipo: url
    requerido: false
    descripcion: "URL del logotipo corporativo"
  
  imagen_fondo_url:
    tipo: url
    requerido: false
    descripcion: "Imagen de fondo de portada"
```

#### 0.3 RESUMEN EJECUTIVO

```yaml
resumen_ejecutivo:
  que_es_negocio:
    tipo: text
    requerido: true
    max_caracteres: 500
    descripcion: "Descripción concisa del producto/servicio"
  
  como_funciona:
    tipo: text
    requerido: true
    max_caracteres: 500
    descripcion: "Breve explicación del modelo de negocio"
  
  con_que_recursos:
    tipo: text
    requerido: true
    max_caracteres: 500
    descripcion: "Recursos clave e inversión inicial"
  
  para_que_mercado:
    tipo: text
    requerido: true
    max_caracteres: 500
    descripcion: "Segmento objetivo y tamaño del mercado"
  
  cuanto_inversion:
    tipo: decimal
    requerido: true
    precision: 2
    moneda: "BOB"
    descripcion: "Inversión inicial total requerida"
  
  roi_esperado:
    tipo: decimal
    requerido: false
    precision: 2
    descripcion: "Retorno sobre inversión esperado (%)"
  
  punto_equilibrio_meses:
    tipo: integer
    requerido: false
    descripcion: "Meses para alcanzar punto de equilibrio"
  
  equipo_clave:
    tipo: array[string]
    requerido: false
    descripcion: "Nombres o cargos del equipo fundador"
  
  uso_fondos:
    tipo: json
    requerido: false
    descripcion: "Distribución de la inversión"
    estructura:
      inversion_fija: decimal
      capital_trabajo: decimal
      gastos_preoperativos: decimal
```

---

### I. DEFINICIÓN DEL NEGOCIO

#### 1.1.1 IDEA DE NEGOCIO

```yaml
idea_negocio:
  concepto_negocio:
    tipo: text
    requerido: true
    max_caracteres: 2000
    descripcion: "Descripción completa de qué es y qué hace el negocio"
  
  sector_industria:
    tipo: enum
    requerido: true
    opciones:
      - "Gastronomía"
      - "Tecnología"
      - "Retail"
      - "Servicios"
      - "Manufactura"
      - "Agroindustria"
      - "Salud"
      - "Educación"
      - "Turismo"
      - "Otro"
  
  subsector_especifico:
    tipo: string
    requerido: true
    descripcion: "Subcategoría específica"
    ejemplo: "Cafetería especializada"
  
  tipo_negocio:
    tipo: enum
    requerido: true
    opciones: ["producto", "servicio", "producto_y_servicio"]
  
  modelo_negocio_b2:
    tipo: enum
    requerido: true
    opciones: ["B2B", "B2C", "B2B2C", "B2G"]
    descripcion: "Business to Business / Business to Consumer"
  
  canal_principal:
    tipo: enum
    requerido: true
    opciones: ["online", "offline", "omnicanal"]
  
  origen_idea:
    tipo: text
    requerido: true
    descripcion: "¿Por qué surgió esta oportunidad de negocio?"
  
  problema_resuelve:
    tipo: text
    requerido: true
    descripcion: "¿Qué problema resuelve o necesidad satisface?"
```

#### 1.1.2 MISIÓN Y VISIÓN

```yaml
mision_vision:
  mision_declaracion:
    tipo: text
    requerido: true
    max_caracteres: 500
    descripcion: "Qué hace la empresa hoy, para quién y cómo"
    ejemplo: "Somos una cafetería dedicada a ofrecer café de especialidad de origen boliviano a jóvenes profesionales de La Paz, mediante un ambiente acogedor y atención personalizada"
  
  vision_declaracion:
    tipo: text
    requerido: true
    max_caracteres: 500
    descripcion: "Dónde quiere estar la empresa en 3-5 años"
    ejemplo: "Ser la cadena de cafeterías de especialidad líder en Bolivia, reconocida por la calidad de nuestro café orgánico y el impacto social en comunidades productoras"
  
  valores_corporativos:
    tipo: array[object]
    requerido: true
    min_items: 3
    max_items: 5
    estructura:
      valor:
        tipo: string
        ejemplo: "Calidad"
      descripcion:
        tipo: text
        max_caracteres: 200
        ejemplo: "Compromiso con la excelencia en cada taza de café que servimos"
  
  proposito_existencia:
    tipo: text
    requerido: false
    descripcion: "Por qué existe la empresa más allá de ganar dinero (Golden Circle - Simon Sinek)"
```

#### 1.1.3 PROPUESTA DE VALOR

```yaml
propuesta_valor:
  problema_cliente:
    tipo: text
    requerido: true
    max_caracteres: 1000
    descripcion: "¿Qué dolor o frustración resuelve?"
  
  solucion_ofrecida:
    tipo: text
    requerido: true
    max_caracteres: 1000
    descripcion: "¿Qué beneficio concreto entrega?"
  
  diferenciador_clave:
    tipo: text
    requerido: true
    max_caracteres: 1000
    descripcion: "¿Por qué elegirte vs. la competencia?"
  
  beneficio_emocional:
    tipo: string
    requerido: false
    descripcion: "Beneficio no tangible (ej: status, pertenencia)"
  
  beneficio_funcional:
    tipo: string
    requerido: true
    descripcion: "Beneficio práctico y medible"
```

#### 1.2.1 CANVAS DE 9 MÓDULOS

```yaml
canvas_negocio:
  segmento_clientes:
    descripcion: "¿Quiénes son tus clientes?"
    perfil_detallado: text
    caracteristicas: array[string]
  
  propuesta_valor_canvas:
    descripcion: "¿Qué valor entregas?"
    productos_servicios: array[string]
    resolvedores_dolor: array[string]
    creadores_ganancia: array[string]
  
  canales_distribucion:
    descripcion: "¿Cómo llegas a ellos?"
    canales_venta: array[string]
    canales_comunicacion: array[string]
  
  relacion_clientes:
    descripcion: "¿Cómo interactúas con ellos?"
    tipo_relacion: enum["personal_asistida", "auto_servicio", "comunidad", "co_creacion"]
    estrategia_retencion: text
  
  fuentes_ingreso:
    descripcion: "¿Cómo ganas dinero?"
    modelo_ingreso: enum["venta_activo", "suscripcion", "comision", "publicidad", "freemium"]
    precio_unitario: decimal
    volumen_esperado: integer
  
  recursos_clave:
    descripcion: "¿Qué necesitas para operar?"
    recursos_fisicos: array[string]
    recursos_humanos: array[string]
    recursos_intelectuales: array[string]
    recursos_financieros: array[string]
  
  actividades_clave:
    descripcion: "¿Qué haces día a día?"
    actividades_produccion: array[string]
    actividades_marketing: array[string]
    actividades_logistica: array[string]
    actividades_postventa: array[string]
  
  socios_clave:
    descripcion: "¿Quiénes te ayudan?"
    proveedores: array[string]
    aliados_estrategicos: array[string]
    distribuidores: array[string]
  
  estructura_costos:
    descripcion: "¿En qué gastas?"
    costos_fijos_mensuales: array[object]
      - concepto: string
      - monto: decimal
    costos_variables_unitarios: array[object]
      - concepto: string
      - monto: decimal
```

---

### II. ANÁLISIS DEL ENTORNO Y MERCADO

#### 2.1 PESTEL

```yaml
analisis_pestel:
  politico_legal:
    estabilidad_politica: text
    regulaciones_sector: array[string]
    impuestos_aplicables: array[string]
    normas_laborales: text
    proteccion_consumidor: text
    fuentes_datos: array[url]
  
  economico:
    pib_pais: decimal
    crecimiento_pib: decimal
    inflacion_actual: decimal
    inflacion_proyectada: decimal
    tipo_cambio: decimal
    tasa_interes: decimal
    poder_adquisitivo_segmento: text
  
  socio_cultural:
    demografia: json
      edad_promedio: integer
      tamaño_hogar: decimal
      distribucion_geografica: text
    estilos_vida: array[string]
    valores_culturales: array[string]
    nivel_educativo: text
    habitos_compra: json
      frecuencia: string
      canales_preferidos: array[string]
      decision_individual_familiar: enum["individual", "familiar", "mixto"]
  
  tecnologico:
    penetracion_internet: decimal
    penetracion_smartphones: decimal
    adopcion_digital_sector: text
    innovaciones_disruptivas: array[string]
    logistica_cadena_suministro: text
  
  ecologico:
    regulaciones_ambientales: array[string]
    expectativas_sostenibilidad: text
    huella_carbono_negocio: text
    gestion_residuos: text
  
  fuentes_citadas: array[object]
    - nombre_fuente: string
    - url: url
    - fecha_consulta: date
```

#### 2.2 PORTER 5 FUERZAS

```yaml
porter_cinco_fuerzas:
  amenaza_nuevos_entrantes:
    nivel_amenaza: enum["baja", "media", "alta"]
    barreras_entrada: json
      economicas: text
      tecnologicas: text
      legales: text
      marca_lealtad: text
      escala: text
    analisis_detallado: text
  
  poder_proveedores:
    nivel_poder: enum["bajo", "medio", "alto"]
    numero_proveedores: integer
    diferenciacion_insumos: text
    costo_cambio_proveedor: text
    integracion_atras: boolean
  
  poder_clientes:
    nivel_poder: enum["bajo", "medio", "alto"]
    numero_clientes: enum["muchos", "pocos", "concentrados"]
    diferenciacion_producto: text
    costo_cambio_cliente: text
    informacion_disponible: text
  
  amenaza_sustitutos:
    nivel_amenaza: enum["baja", "media", "alta"]
    alternativas_existen: array[string]
    relacion_calidad_precio: text
    costo_cambio_sustituto: text
  
  rivalidad_competidores:
    nivel_rivalidad: enum["baja", "media", "alta", "intensa"]
    numero_competidores: integer
    crecimiento_mercado: enum["crecimiento", "madurez", "saturacion"]
    diferenciacion_ofertas: text
    barreras_salida: text
  
  benchmarking_competidores:
    tipo: array[object]
    estructura:
      nombre_competidor: string
      tipo: enum["directo", "indirecto"]
      producto_servicio: text
      precio_aproximado: decimal
      canales: array[string]
      fortaleza_clave: text
      debilidad_clave: text
      posicionamiento: text
      cuota_mercado_estimada: decimal
```

#### 2.3 FODA

```yaml
analisis_foda:
  fortalezas:
    tipo: array[object]
    items:
      - descripcion: string
      - impacto: enum["alto", "medio", "bajo"]
      - duracion: enum["corto", "medio", "largo"]
  
  oportunidades:
    tipo: array[object]
    items:
      - descripcion: string
      - probabilidad: enum["alta", "media", "baja"]
      - impacto_potencial: enum["alto", "medio", "bajo"]
  
  debilidades:
    tipo: array[object]
    items:
      - descripcion: string
      - criticidad: enum["alta", "media", "baja"]
      - plan_mitigacion: text
  
  amenazas:
    tipo: array[object]
    items:
      - descripcion: string
      - probabilidad: enum["alta", "media", "baja"]
      - plan_contingencia: text
  
  estrategias_fo:
    tipo: array[string]
    descripcion: "Fortalezas + Oportunidades (Estrategias Ofensivas)"
  
  estrategias_do:
    tipo: array[string]
    descripcion: "Debilidades + Oportunidades (Estrategias Adaptativas)"
  
  estrategias_fa:
    tipo: array[string]
    descripcion: "Fortalezas + Amenazas (Estrategias Defensivas)"
  
  estrategias_da:
    tipo: array[string]
    descripcion: "Debilidades + Amenazas (Estrategias de Supervivencia)"
```

#### 2.4 BUYER PERSONA

```yaml
buyer_persona:
  identidad_ficticia:
    nombre_ficticio: string
    edad: integer
    genero: enum["masculino", "femenino", "no_binario", "no_especifica"]
    ocupacion: string
    nivel_socioeconomico: enum["bajo", "medio_bajo", "medio", "medio_alto", "alto"]
    ubicacion_geografica: string
    situacion_familiar: text
  
  psicografia:
    motivaciones: array[string]
    frustraciones_puntos_dolor: array[string]
    objetivos_ganancias: array[string]
    valores_personales: array[string]
    personalidad: enum["innovador", "temprano", "mayoria_temprana", "mayoria_tardia", "rezagado"]
  
  comportamiento:
    habitos_digitales: json
      redes_sociales_usa: array[string]
      frecuencia_redes: enum["diaria", "semanal", "ocasional"]
      dispositivo_principal: enum["smartphone", "computadora", "tablet"]
    canales_informacion: array[string]
    criterios_decision_compra: array[string]
    objeciones_frecuentes: array[string]
    influenciadores: array[string]
  
  journey_compra:
    etapas:
      - nombre: "descubrimiento"
        touchpoints: array[string]
        emocion: string
        fricciones: array[string]
        oportunidades_mejora: array[string]
      - nombre: "evaluacion"
        touchpoints: array[string]
        emocion: string
        fricciones: array[string]
        oportunidades_mejora: array[string]
      - nombre: "decision"
        touchpoints: array[string]
        emocion: string
        fricciones: array[string]
        oportunidades_mejora: array[string]
      - nombre: "postventa"
        touchpoints: array[string]
        emocion: string
        fricciones: array[string]
        oportunidades_mejora: array[string]
```

---

### III. INVESTIGACIÓN DE MERCADO

#### 3.1 ENCUESTA

```yaml
investigacion_encuesta:
  diseno_metodologico:
    objetivo_general: text
    objetivos_especificos: array[string]
    enfoque: enum["exploratorio", "descriptivo", "causal", "mixto"]
    tipo_datos: enum["cualitativos", "cuantitativos", "mixto"]
  
  poblacion_muestra:
    universo_objetivo: text
    tamano_muestra: integer
    metodo_muestreo: enum["aleatorio_simple", "aleatorio_sistematico", "estratificado", "por_conveniencia"]
    nivel_confianza: decimal
    margen_error: decimal
  
  instrumento:
    numero_preguntas: integer
    tiempo_estimado_minutos: integer
    escala_medicion: enum["likert", "nominal", "ordinal", "intervalo", "razon"]
    secciones:
      - filtros: array[object]
      - habitos_consumo: array[object]
      - percepcion_marcas: array[object]
      - evaluacion_propuesta: array[object]
      - disposicion_pagar: array[object]
      - datos_demograficos: array[object]
  
  trabajo_campo:
    periodo_recoleccion: date_range
    tasa_respuesta: decimal
    tecnicas_control_calidad: array[string]
  
  resultados:
    tabulacion_cruzada: json
    estadistica_descriptiva: json
    hallazgos_clave: array[text]
    validacion_hipotesis: array[object]
    conclusiones: text
```

#### 3.2 TAM/SAM/SOM

```yaml
analisis_demanda:
  tam_total_addressable_market:
    valor_moneda_local: decimal
    valor_usd: decimal
    poblacion_total: integer
    consumo_per_capita: decimal
    precio_promedio: decimal
    metodologia_calculo: text
    fuentes: array[string]
  
  sam_serviceable_available_market:
    valor_moneda_local: decimal
    valor_usd: decimal
    porcentaje_poblacion_objetivo: decimal
    porcentaje_zona_geografica: decimal
    metodologia_calculo: text
  
  som_serviceable_obtainable_market:
    valor_moneda_local: decimal
    valor_usd: decimal
    porcentaje_penetracion_realista: decimal
    capacidad_produccion_limite: integer
    year_1: decimal
    year_2: decimal
    year_3: decimal
  
  proyeccion_ventas:
    year_1:
      unidades: integer
      precio_unitario: decimal
      ventas_totales: decimal
      crecimiento: decimal
    year_2:
      unidades: integer
      precio_unitario: decimal
      ventas_totales: decimal
      crecimiento: decimal
    year_3:
      unidades: integer
      precio_unitario: decimal
      ventas_totales: decimal
      crecimiento: decimal
    supuestos: text
```

---

## 📊 TABLAS AUXILIARES REQUERIDAS

### tabla_planes (Entidad Principal)
```yaml
plan_negocio:
  id: uuid (PK)
  nombre_proyecto: string
  autor_id: uuid (FK)
  estado: enum["borrador", "en_progreso", "completado", "archivado"]
  version: string
  fecha_creacion: datetime
  fecha_actualizacion: datetime
  tono_configuracion: json
  metadata: json
```

### tabla_usuarios
```yaml
usuario:
  id: uuid (PK)
  nombre_completo: string
  email: string (unique)
  nivel_academico: enum
  perfil_profesional: text
  preferencias_generacion: json
```

### tabla_secciones_generadas
```yaml
seccion_generada:
  id: uuid (PK)
  plan_id: uuid (FK)
  capitulo: string
  subcapitulo: string
  contenido_generado: text
  fuentes_utilizadas: array[url]
  estado_revision: enum["pendiente", "aprobado", "rechazado", "modificar"]
  comentarios_revision: text
  fecha_generacion: datetime
```

---

## 🎯 RELACIONES ENTRE TABLAS

```
usuario (1) ----< (N) planes_negocio
                    |
                    |----< (N) secciones_generadas
                    |
                    |---- (1) portada
                    |---- (1) resumen_ejecutivo
                    |---- (1) idea_negocio
                    |---- (1) mision_vision
                    |---- (1) canvas_negocio
                    |---- (1) analisis_pestel
                    |---- (1) porter_cinco_fuerzas
                    |---- (1) analisis_foda
                    |---- (1) buyer_persona
                    |---- (1) investigacion_encuesta
                    |---- (1) analisis_demanda
                    +---- ... (demás secciones)
```

---

*Esquema de Base de Datos - BPAE v1.0*
