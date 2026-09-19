<div align="center">



<h3>Universidad Peruana de Ciencias Aplicadas</h3>

<strong>Facultad de Ingeniería</strong><br>
<strong>Carrera: Ingeniería de Software</strong><br>

<strong>Periodo:</strong> 202620<br>
<strong>Codigo del curso:</strong>  1ASI057 <br>
<strong>Nombre del curso:</strong>  Desarrollo de Soluciones IoT<br>
<strong>NRC:</strong> 8725 <br>

<strong>Nombre del profesor:</strong> Marco Antonio León Baca <br>

<br><strong>*Informe de Trabajo Final*</strong><br><br>

<strong>Nombre del startup: </strong>FreshEat<br>
<strong>Nombre del producto: </strong>FreshSense<br>



### Relación de Integrantes

| Apellidos y Nombres                  |   Código    |
|:------------------------------------:|:-----------:|
| Tuesta Marin, Romina Alejandra       | U202211706  |

<strong> Septiembre 2026</strong><br>
</div>

<div style="page-break-after: always;"></div>

# Project Report Collaboration Insights

**AV1:**
![pcav1](assets/.png)


<div style="page-break-after: always;"></div>

# Registro de Versiones del Informe

| Versión | Fecha      | Autor        | Descripción de modificación                   |
|---------|------------|--------------|-----------------------------------------------|
| 1.0     | 08/09/2026 | Romina Tuesta Marin | Cargó archivos, Descripción de la Startup|


# Tabla de contenidos

- [Student Outcome](#student-outcome)

- [Capítulo I: Introducción](#capítulo-i-introducción)
  - [1.1. Startup Profile](#11-startup-profile)
    - [1.1.1. Descripción de la Startup](#111-descripción-de-la-startup)
    - [1.1.2. Perfiles de integrantes del equipo](#112-perfiles-de-integrantes-del-equipo)
  - [1.2. Solution Profile](#12-solution-profile)
    - [1.2.1. Antecedentes y problemática](#121-antecedentes-y-problemática)
    - [1.2.2. Lean UX Process](#122-lean-ux-process)
      - [1.2.2.1. Lean UX Problem Statements](#1221-lean-ux-problem-statements)
      - [1.2.2.2. Lean UX Assumptions](#1222-lean-ux-assumptions)
      - [1.2.2.3. Lean UX Hypothesis Statements](#1223-lean-ux-hypothesis-statements)
      - [1.2.2.4. Lean UX Canvas](#1224-lean-ux-canvas)
  - [1.3. Segmentos objetivo](#13-segmentos-objetivo)

- [Capítulo II: Requirements Elicitation & Analysis](#capítulo-ii-requirements-elicitation--analysis)
  - [2.1. Competidores](#21-competidores)
    - [2.1.1. Análisis competitivo](#211-análisis-competitivo)
    - [2.1.2. Estrategias y tácticas frente a competidores](#212-estrategias-y-tácticas-frente-a-competidores)
  - [2.2. Entrevistas](#22-entrevistas)
    - [2.2.1. Diseño de entrevistas](#221-diseño-de-entrevistas)
    - [2.2.2. Registro de entrevistas](#222-registro-de-entrevistas)
    - [2.2.3. Análisis de entrevistas](#223-análisis-de-entrevistas)
  - [2.3. Needfinding](#23-needfinding)
    - [2.3.1. User Personas](#231-user-personas)
    - [2.3.2. User Task Matrix](#232-user-task-matrix)
    - [2.3.3. User Journey Mapping](#233-user-journey-mapping)
    - [2.3.4. Empathy Mapping](#234-empathy-mapping)
  - [2.4. Big Picture EventStorming](#24-big-picture-eventstorming)
  - [2.5. Ubiquitous Language](#25-ubiquitous-language)

- [Capítulo III: Requirements Specification](#capítulo-iii-requirements-specification)
  - [3.1. User Stories](#31-user-stories)
  - [3.2. Impact Mapping](#32-impact-mapping)
  - [3.3. Product Backlog](#33-product-backlog)

- [Capítulo IV: Solution Software Design](#capítulo-iv-solution-software-design)
  - [4.1. Strategic-Level Domain-Driven Design](#41-strategic-level-domain-driven-design)
    - [4.1.1. Design-Level EventStorming](#411-design-level-eventstorming)
      - [4.1.1.1. Candidate Context Discovery](#4111-candidate-context-discovery)
      - [4.1.1.2. Domain Message Flows Modeling](#4112-domain-message-flows-modeling)
      - [4.1.1.3. Bounded Context Canvases](#4113-bounded-context-canvases)
    - [4.1.2. Context Mapping](#412-context-mapping)
    - [4.1.3. Software Architecture](#413-software-architecture)
      - [4.1.3.1. Software Architecture System Landscape Diagram](#4131-software-architecture-system-landscape-diagram)
      - [4.1.3.2. Software Architecture Context Level Diagrams](#4132-software-architecture-context-level-diagrams)
      - [4.1.3.2. Software Architecture Container Level Diagrams](#4132-software-architecture-container-level-diagrams)
      - [4.1.3.3. Software Architecture Deployment Diagrams](#4133-software-architecture-deployment-diagrams)
  - [4.2. Tactical-Level Domain-Driven Design](#42-tactical-level-domain-driven-design)
    - [4.2.X. Bounded Context: &lt;Bounded Context Name&gt;](#42x-bounded-context-bounded-context-name)
      - [4.2.X.1. Domain Layer](#42x1-domain-layer)
      - [4.2.X.2. Interface Layer](#42x2-interface-layer)
      - [4.2.X.3. Application Layer](#42x3-application-layer)
      - [4.2.X.4. Infrastructure Layer](#42x4-infrastructure-layer)
      - [4.2.X.5. Bounded Context Software Architecture Component Level Diagrams](#42x5-bounded-context-software-architecture-component-level-diagrams)
      - [4.2.X.6. Bounded Context Software Architecture Code Level Diagrams](#42x6-bounded-context-software-architecture-code-level-diagrams)
        - [4.2.X.6.1. Bounded Context Domain Layer Class Diagrams](#42x61-bounded-context-domain-layer-class-diagrams)
        - [4.2.X.6.2. Bounded Context Database Design Diagram](#42x62-bounded-context-database-design-diagram)

- [Capítulo V: Solution UI/UX Design](#capítulo-v-solution-uiux-design)
  - [5.1. Style Guidelines](#51-style-guidelines)
    - [5.1.1. General Style Guidelines](#511-general-style-guidelines)
    - [5.1.2. Web, Mobile and IoT Style Guidelines](#512-web-mobile-and-iot-style-guidelines)
  - [5.2. Information Architecture](#52-information-architecture)
    - [5.2.1. Organization Systems](#521-organization-systems)
    - [5.2.2. Labeling Systems](#522-labeling-systems)
    - [5.2.3. SEO Tags and Meta Tags](#523-seo-tags-and-meta-tags)
    - [5.2.4. Searching Systems](#524-searching-systems)
    - [5.2.5. Navigation Systems](#525-navigation-systems)
  - [5.3. Landing Page UI Design](#53-landing-page-ui-design)
    - [5.3.1. Landing Page Wireframe](#531-landing-page-wireframe)
    - [5.3.2. Landing Page Mock-up](#532-landing-page-mock-up)
  - [5.4. Applications UX/UI Design](#54-applications-uxui-design)
    - [5.4.1. Applications Wireframes](#541-applications-wireframes)
    - [5.4.2. Applications Wireflow Diagrams](#542-applications-wireflow-diagrams)
    - [5.4.2. Applications Mock-ups](#542-applications-mock-ups)
    - [5.4.3. Applications User Flow Diagrams](#543-applications-user-flow-diagrams)
  - [5.5. Applications Prototyping](#55-applications-prototyping)
  - [5.6. IoT Device Design](#56-iot-device-design)

- [Capítulo VI: Product Implementation, Validation & Deployment](#capítulo-vi-product-implementation-validation--deployment)
  - [6.1. Software Configuration Management](#61-software-configuration-management)
    - [6.1.1. Software Development Environment Configuration](#611-software-development-environment-configuration)
    - [6.1.2. Source Code Management](#612-source-code-management)
    - [6.1.3. Source Code Style Guide & Conventions](#613-source-code-style-guide--conventions)
    - [6.1.4. Software Deployment Configuration](#614-software-deployment-configuration)
  - [6.2. Landing Page, Services & Applications Implementation](#62-landing-page-services--applications-implementation)
    - [6.2.X. Sprint n](#62x-sprint-n)
      - [6.2.X.1. Sprint Planning n](#62x1-sprint-planning-n)
      - [6.2.X.2. Aspect Leaders and Collaborators](#62x2-aspect-leaders-and-collaborators)
      - [6.2.X.3. Sprint Backlog n](#62x3-sprint-backlog-n)
      - [6.2.X.4. Development Evidence for Sprint Review](#62x4-development-evidence-for-sprint-review)
      - [6.2.X.5. Testing Suite Evidence for Sprint Review](#62x5-testing-suite-evidence-for-sprint-review)
      - [6.2.X.6. Execution Evidence for Sprint Review](#62x6-execution-evidence-for-sprint-review)
      - [6.2.X.7. Services Documentation Evidence for Sprint Review](#62x7-services-documentation-evidence-for-sprint-review)
      - [6.2.X.8. Software Deployment Evidence for Sprint Review](#62x8-software-deployment-evidence-for-sprint-review)
      - [6.2.X.9. Team Collaboration Insights during Sprint](#62x9-team-collaboration-insights-during-sprint)
  - [6.3. Validation Interviews](#63-validation-interviews)
    - [6.3.1. Diseño de Entrevistas](#631-diseño-de-entrevistas)
    - [6.3.2. Registro de Entrevistas](#632-registro-de-entrevistas)
    - [6.3.3. Evaluaciones según heurísticas](#633-evaluaciones-según-heurísticas)
  - [6.4. Video About-the-Product](#64-video-about-the-product)

- [Conclusiones](#conclusiones)
- [Conclusiones y recomendaciones](#conclusiones-y-recomendaciones)
- [Video About-the-Team](#video-about-the-team)
- [Bibliografía](#bibliografía)
- [Anexos](#anexos)

## Student Outcome

El curso contribuye al cumplimiento del Student Outcome ABET:
ABET – EAC - Student Outcome 5
Criterio: La capacidad de funcionar efectivamente en un equipo cuyos miembros
juntos proporcionan liderazgo, crean un entorno de colaboración e inclusivo,
establecen objetivos, planifican tareas y cumplen objetivos.
En el siguiente cuadro se describe las acciones realizadas y enunciados de
conclusiones por parte del grupo, que permiten sustentar el haber alcanzado el logro
del ABET – EAC - Student Outcome 5.

| Criterio específico | Acciones realizadas | Conclusiones |
| :---- | :---- | :---- |
| Trabaja en equipo para proporcionar liderazgo en forma conjunta | **AV1:** <br> **Romina Tuesta Marin:** Se distribuyeron responsabilidades entre los integrantes según sus habilidades, coordinando las actividades de análisis, diseño, desarrollo y documentación. Asimismo, se tomaron decisiones de manera conjunta y se realizó seguimiento al avance de cada tarea.   | **AV1:** <br> El trabajo colaborativo permitió aprovechar las habilidades de cada integrante, mantener una participación activa y avanzar de manera coordinada hacia los objetivos del proyecto. |
| Crea un entorno colaborativo e inclusivo, establece metas, planifica tareas y cumple objetivos | **AV1:** <br> **Romina Tuesta Marin:** Se establecieron objetivos y tareas para cada integrante, organizando las actividades de acuerdo con las prioridades del proyecto. Se mantuvo una comunicación constante para resolver dudas, compartir avances y realizar ajustes cuando fue necesario. | **AV1:** La planificación y comunicación constante facilitaron la coordinación del equipo, permitiendo cumplir las actividades asignadas y mantener el avance del proyecto de acuerdo con los objetivos establecidos.|

<div style="page-break-after: always;"></div>

## Capítulo I: Introducción

### 1.1. Startup Profilee

### 1.1.1. Descripción de la Startup

FreshSense es una startup de tecnología orientada a ayudar a restaurantes y negocios de alimentos fríos a reducir las pérdidas económicas ocasionadas por el deterioro y desperdicio de productos perecibles. La solución combina una aplicación de gestión de inventario con dispositivos de monitoreo para supervisar las condiciones de conservación de los alimentos y generar alertas oportunas ante situaciones que puedan afectar su calidad.

FreshSense permite a los negocios conocer el estado de sus productos, gestionar su inventario y recibir información que facilite la toma de decisiones sobre conservación, rotación y aprovechamiento de los alimentos. De esta manera, busca reducir las mermas, disminuir costos innecesarios y contribuir a mejorar la rentabilidad de los negocios.

La startup plantea un modelo de negocio basado en la comercialización de los dispositivos de monitoreo y una suscripción para acceder a funcionalidades avanzadas de la plataforma, como reportes, análisis del inventario y seguimiento de pérdidas.

### 1.1.2. Perfiles de integrantes del equipo

### 1.2. Solution Profile

### 1.2.1 Antecedentes y problemática

El desperdicio de alimentos es un problema grave en el Perú tanto a nivel económico como ambiental. Según la información explicada en el II Foro Nacional de la Recuperación de Alimentos y Conmemoración del Día de Concienciación sobre la Pérdida y el Desperdicio de Alimentos en el Perú, realizado por la FOA (Organización de la Naciones Unidas para la Alimentación y la Agricultura) junto con MIDAGRI (Ministerio de Desarrollo Agrario y Riego) y PMA (Programa Mundial de Alimentos), en el país, 12.8 millones de toneladas de alimentos se pierden en la cadena de producción (FOA, 2024). Es un número muy preocupante considerando que el 51% de las familias peruanas está en situación de inseguridad alimentaria (Blas, 2022). A partir de ello, es claro que hay una relaciónestrecha entre el desperdicio de alimentos y la inseguridad alimentaria; el gobierno se está encargando de mitigar tal desperdicio mediante foros, proyectos, etc. Teniendo en cuenta este contexto, Enrique Román, representante asistente de FAO en Perú señala que los hogares peruanos representan el 16% en el desperdicio de alimentos (FAO, 2024), un porcentaje alarmante. Más aún, acorde a Alberto Huiman, doctor en Ciencias Ambientales, cada peruano genera un desperdicio de 67 kilogramos por año y los restaurantes es alrededor de 500 kilogramos por día. Esto complica gravemente la situación del país respecto a las pérdidas en el aspecto de alimentos.  

Para analizar con más detalle los antecedentes y problemáticas, se realizó con anticipación la técnica 5 ‘W’s & 2 ‘H’s:

## What? (¿Qué es?)

FreshSense es una aplicación web orientada a restaurantes y negocios de alimentos fríos que permite monitorear y gestionar el inventario de productos perecibles. Mediante alertas y notificaciones, ayuda a detectar oportunamente condiciones que pueden ocasionar el deterioro de los alimentos, facilitando decisiones para reducir mermas y pérdidas económicas.

#### Why? (¿Por qué?)

La falta de información precisa y oportuna sobre las condiciones de conservación de los alimentos dificulta detectar su deterioro antes de que se convierta en una pérdida. Esto puede generar desperdicio de productos, costos de reposición y una reducción de la rentabilidad del negocio.

#### Where? (¿Dónde?)

FreshSense está orientada a restaurantes y negocios de alimentos fríos, principalmente en espacios donde se almacenan productos perecibles, como refrigeradores, congeladores, cámaras de frío y almacenes.

#### When? (¿Cuándo?)

El problema ocurre durante el almacenamiento y conservación de los productos, especialmente cuando permanecen durante periodos prolongados sin un monitoreo adecuado de sus condiciones. FreshSense permite realizar un seguimiento continuo y recibir alertas para tomar decisiones oportunas.

#### Who? (¿Quién?)

Los principales usuarios de FreshSense son los propietarios, administradores y encargados de restaurantes, así como los responsables de negocios de alimentos fríos que necesitan controlar la conservación de sus productos, reducir mermas y proteger la rentabilidad del negocio.

#### How? (¿Cómo?)

FreshSense busca facilitar la gestión y conservación de los productos mediante:

* Registro y gestión del inventario de alimentos.
* Monitoreo de condiciones de conservación mediante sensores.
* Alertas ante condiciones que puedan afectar los productos.
* Notificaciones sobre productos próximos a deteriorarse o vencer.
* Reportes sobre pérdidas, rotación y estado del inventario.
* Sugerencias para aprovechar productos antes de que representen una pérdida económica.
* Acceso a la información desde diferentes dispositivos.

#### How much? (¿Cuánto?)

El desperdicio y deterioro de alimentos representa una pérdida económica para los negocios, ya que implica desechar productos que fueron adquiridos para su comercialización o utilización. FreshSense busca reducir estas pérdidas mediante el monitoreo y gestión preventiva del inventario.

El modelo de negocio considera:

* Suscripción mensual o anual para acceder a funcionalidades avanzadas.
* Venta del dispositivo sensor como pago único.
* Funcionalidades premium orientadas al análisis del inventario y las pérdidas económicas.

### 1.2.2 Lean UX Process.

### 1.2.2.1. Lean UX Problem Statements.

Los restaurantes y negocios de alimentos fríos pueden sufrir pérdidas económicas debido al deterioro de productos perecibles que no es detectado oportunamente. La falta de monitoreo continuo de las condiciones de conservación dificulta tomar decisiones preventivas sobre el inventario, generando mermas, costos de reposición y reducción de la rentabilidad.

La gestión manual del inventario y las condiciones de conservación también dificulta conocer en tiempo real qué productos presentan mayor riesgo de deterioro y cuáles requieren atención prioritaria.

**Creemos que** reducir el desperdicio de alimentos permitirá a los negocios disminuir sus pérdidas económicas y mejorar su rentabilidad. **Sabremos que esto es cierto cuando** se observe una reducción medible de las pérdidas asociadas al deterioro de productos durante el periodo de evaluación.

**Creemos que** las alertas sobre condiciones de conservación y productos próximos a deteriorarse ayudarán a los usuarios a tomar decisiones oportunas. 
**Sabremos que esto es cierto cuando** los usuarios utilicen las alertas para realizar acciones preventivas sobre los productos identificados.

**Creemos que** permitir el acceso a la aplicación desde diferentes dispositivos facilitará el monitoreo del inventario durante la operación diaria. 
**Sabremos que esto es cierto cuando** los usuarios consulten regularmente el estado de sus productos desde al menos dos tipos de dispositivos.

**Creemos que** los reportes de pérdidas y rotación de inventario ayudarán a los administradores a identificar oportunidades para reducir mermas. **Sabremos que esto es cierto cuando** los usuarios consulten estos reportes para tomar decisiones relacionadas con su inventario.

### 1.2.2.2. Lean UX Assumptions.

##### Business Assumptions

* Creemos que nuestros usuarios necesitan una solución que les permita monitorear las condiciones de conservación de sus productos y gestionar su inventario para reducir pérdidas económicas. 

*  Estas necesidades pueden resolverse mediante una aplicación que centralice el inventario, las alertas de conservación y los reportes de pérdidas en una interfaz sencilla y accesible.

*  Nuestros clientes iniciales son restaurantes y negocios de alimentos fríos que manejan productos perecibles y buscan reducir mermas y proteger la rentabilidad de sus operaciones.

* El principal valor que el cliente requiere de FreshSense es conocer oportunamente el estado de sus productos para tomar decisiones antes de que estos representen una pérdida económica.

* Como beneficios adicionales, el cliente podrá acceder a reportes de inventario, análisis de pérdidas, alertas preventivas y recomendaciones para aprovechar productos próximos a deteriorarse.

* Adquiriremos clientes mediante una landing page, demostraciones del producto, marketing digital y estrategias de venta directa orientadas a los segmentos objetivo.

* Generaremos ingresos mediante la venta del dispositivo sensor y suscripciones para acceder a funcionalidades avanzadas.

* Nuestra competencia incluye métodos manuales de control de inventario, hojas de cálculo y sistemas genéricos de gestión de inventario.
  
* Nos diferenciaremos mediante una solución especializada en la conservación de productos perecibles, que combine monitoreo, alertas y gestión del inventario.

* Nuestros principales riesgos son la resistencia al cambio tecnológico, la preferencia por métodos manuales, el costo percibido de la solución y la dificultad para incorporar el sistema en las actividades diarias del negocio.

* Reduciremos estos riesgos mediante una interfaz sencilla, procesos de registro rápidos, funcionalidades enfocadas en las necesidades principales del usuario y una implementación que requiera la menor cantidad posible de cambios en su rutina.

* Sabremos que hemos tenido éxito cuando los negocios usuarios reduzcan sus pérdidas asociadas al deterioro de alimentos y utilicen regularmente la aplicación para gestionar su inventario.

##### Business Outcomes

* Reducir las pérdidas económicas ocasionadas por el deterioro de alimentos.
* Disminuir la merma de productos perecibles.
* Mejorar la rentabilidad de los negocios mediante una gestión eficiente del inventario.
* Lograr la adopción y retención de usuarios mediante una solución simple y útil.
* Generar ingresos recurrentes mediante la venta del dispositivo y suscripción premium.
* Validar un modelo de negocio escalable para restaurantes y negocios de alimentos fríos.

##### User Assumptions

###### ¿Quiénes serán nuestros usuarios?

**Nuestros usuarios principales son:**

* Propietarios y administradores de restaurantes que necesitan controlar sus insumos perecibles y reducir pérdidas económicas.
* Propietarios y encargados de negocios de alimentos fríos que necesitan monitorear la conservación de sus productos y reducir mermas.

###### ¿Dónde encaja nuestro producto en su vida o trabajo?

Para los restaurantes, FreshSense se integra en la gestión diaria de insumos, permitiendo conocer el estado de los productos, recibir alertas y tomar decisiones para evitar pérdidas.

Para los negocios de alimentos fríos, FreshSense se integra en el proceso de almacenamiento y conservación, proporcionando información sobre las condiciones de los productos y alertando ante situaciones que puedan generar pérdidas.

###### ¿Qué problemas tiene nuestro producto y cómo se pueden resolver?

**Problemas:**

* El control del inventario y conservación puede realizarse mediante inspecciones manuales o registros poco actualizados.
* Los usuarios pueden no detectar oportunamente condiciones que afectan la conservación de sus productos.
* El deterioro de alimentos genera merma, costos de reposición y reducción de la rentabilidad.
* El monitoreo manual consume tiempo durante las actividades operativas del negocio.

**Soluciones:**

* Implementar monitoreo de las condiciones de conservación.
* Generar alertas ante condiciones que puedan afectar los productos.
* Mostrar información del inventario de forma clara y accesible.
* Generar reportes que permitan identificar pérdidas y oportunidades de mejora.
* Facilitar decisiones preventivas para reducir la merma.

###### ¿Cómo y cuándo es usado nuestro producto?

FreshSense es utilizada por propietarios, administradores y encargados durante las actividades de almacenamiento, conservación y gestión del inventario. Los usuarios pueden consultar el estado de sus productos, recibir alertas y revisar información sobre pérdidas y rotación durante la jornada operativa.

###### ¿Qué características son importantes?

* Interfaz clara, sencilla y fácil de utilizar.
* Monitoreo de las condiciones de conservación.
* Alertas oportunas ante situaciones de riesgo.
* Gestión rápida del inventario.
* Reportes de pérdidas y rotación.
* Acceso desde diferentes dispositivos.

###### ¿Cómo debe verse y comportarse nuestro producto?

FreshSense debe presentar una interfaz profesional, clara y orientada a la consulta rápida de información crítica. La navegación debe permitir acceder fácilmente al estado del inventario, alertas y reportes sin requerir múltiples pasos.

La aplicación debe estar disponible durante la jornada operativa del negocio y permitir consultas desde dispositivos móviles y computadoras.

##### User Outcomes

* Reducción de pérdidas económicas por deterioro de alimentos.
* Reducción de productos desperdiciados o descartados.
* Mayor frecuencia de monitoreo del inventario.
* Identificación oportuna de productos en riesgo.
* Mejor planificación de compras y reposición.
* Mayor control sobre las condiciones de conservación.
* Mejora de la rentabilidad mediante la reducción de mermas.

##### Features Assumptions

**Desde la cuenta de un restaurante:**

* Registrar alimentos e ingredientes, incluyendo cantidad, fecha de vencimiento y costo.
* Recibir alertas sobre productos próximos a deteriorarse.
* Consultar las condiciones de conservación de los productos.
* Recibir sugerencias para aprovechar productos próximos a deteriorarse.
* Generar reportes de rotación y pérdidas.

**Desde la cuenta de un negocio de alimentos fríos:**

* Registrar productos y cantidades disponibles.
* Monitorear las condiciones de conservación.
* Recibir alertas ante cambios que puedan afectar los productos.
* Identificar productos próximos a deteriorarse o vencer.
* Consultar reportes sobre pérdidas, rotación y estado del inventario.


### 1.2.2.3. Lean UX Hypothesis Statements.

**Creemos que** los restaurantes y negocios de alimentos fríos necesitan una solución que les permita monitorear sus productos y detectar oportunamente condiciones que puedan generar pérdidas económicas.

**Creemos que** las alertas de deterioro y las sugerencias de comercialización ayudarán a los negocios a reducir la merma de productos.

**Creemos que** la carga rápida del inventario facilitará la adopción de la aplicación sin alterar significativamente las actividades diarias de los usuarios.

**Creemos que** los reportes de pérdidas y rotación ayudarán a los administradores a identificar oportunidades para reducir costos y mejorar la rentabilidad.

**Creemos que** una aplicación accesible desde diferentes dispositivos facilitará el monitoreo del inventario durante la operación diaria.

**Sabremos que estas hipótesis son válidas cuando** los usuarios utilicen regularmente las funcionalidades de monitoreo, alertas y reportes, y se observe una reducción medible de las pérdidas económicas asociadas al deterioro de alimentos.

### 1.2.2.4. Lean UX Canvas.

A continuación se presenta el Lean UX Canvas:

![Lean UX Canvas](Assets/LeanUxCanvas.jpg)

### 1.3. Segmentos objetivo.

Para el proyecto FreshSense se han seleccionado dos segmentos principales de usuarios a los cuales la solución aporta un valor adaptado a sus necesidades específicas:

##### Propietarios y Gerentes de Restaurantes Pequeños

**Edad:** 28 a 50 años

**Perfil:** Emprendedores que administran restaurantes pequeños y gestionan insumos perecibles para la preparación de alimentos.

**Estilo de vida:** Dinámico y enfocado en las operaciones diarias, atención al cliente y control del negocio.

**Uso de tecnología:** Frecuente, principalmente mediante dispositivos móviles y computadoras para realizar consultas rápidas.

**Necesidad principal:** Controlar y conservar adecuadamente los insumos perecibles para reducir desperdicios, pérdidas económicas y costos innecesarios.

**Beneficios buscados:** Alertas sobre productos en riesgo de deterioro, monitoreo de las condiciones de conservación, gestión del inventario y reportes que permitan identificar pérdidas y mejorar la rentabilidad.

##### Propietarios y Encargados de Negocios de Alimentos Fríos

**Edad:** 30 a 55 años

**Perfil:** Emprendedores y encargados de negocios dedicados al almacenamiento, conservación y comercialización de productos que requieren cadena de frío.

**Estilo de vida:** Ocupado y enfocado en la operación diaria, supervisión de productos, atención al cliente y gestión del inventario.

**Uso de tecnología:** Moderado a frecuente, con disposición a utilizar herramientas que faciliten el monitoreo y control de sus productos.

**Necesidad principal:** Mantener las condiciones adecuadas de conservación para reducir el deterioro de productos, las mermas y las pérdidas económicas.

**Beneficios buscados:** Monitoreo de las condiciones de conservación, alertas ante posibles riesgos, información sobre el estado del inventario y reportes que permitan identificar pérdidas y mejorar la rentabilidad del negocio.

Capítulo II: Requirements Elicitation & Analysis

2.1. Competidores.

2.1.1. Análisis competitivo.

2.1.2. Estrategias y tácticas frente a competidores.

2.2. Entrevistas.

2.2.1. Diseño de entrevistas.

2.2.2. Registro de entrevistas.

2.2.3. Análisis de entrevistas.

2.3. Needfinding.

### 2.3.1. User Personas.

#### SEGMENTO 1: Adultos jóvenes
![User Person1](assets/José_userP1.png)

### SEGMENTO 2: Pequeños negocios / emprendedores de alimentos caseros
![User Person2](assets/Luisa_userP2.png)


### 2.3.2. User Task Matrix

<table>
  <thead>
    <tr>
      <th rowspan="2">Tareas</th>
      <th colspan="2">José Jimenez<br>(Adulto Joven)</th>
      <th colspan="2">Luisa Pérez<br>(Emprendedora de alimentos)</th>
    </tr>
    <tr>
      <th>Frecuencia</th>
      <th>Importancia</th>
      <th>Frecuencia</th>
      <th>Importancia</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Revisar estado de alimentos en la app</b></td>
      <td>Casi siempre</td>
      <td>Muy alta</td>
      <td>Siempre</td>
      <td>Muy alta</td>
    </tr>
    <tr>
      <td><b>Recibir alertas de vencimiento</b></td>
      <td>Siempre</td>
      <td>Muy alta</td>
      <td>Siempre</td>
      <td>Muy alta</td>
    </tr>
    <tr>
      <td><b>Consultar recetas sugeridas</b></td>
      <td>A veces</td>
      <td>Alta</td>
      <td>Raramente</td>
      <td>Media</td>
    </tr>
    <tr>
      <td><b>Editar inventario manualmente</b></td>
      <td>Raramente</td>
      <td>Media</td>
      <td>Casi siempre</td>
      <td>Alta</td>
    </tr>
    <tr>
      <td><b>Revisar reportes semanales (ahorro, consumo)</b></td>
      <td>A veces</td>
      <td>Media</td>
      <td>Siempre</td>
      <td>Alta</td>
    </tr>
    <tr>
      <td><b>Compartir logros/impacto en redes sociales</b></td>
      <td>A veces</td>
      <td>Media</td>
      <td>Raramente</td>
      <td>Baja</td>
    </tr>
    <tr>
      <td><b>Usar notificaciones configurables (hora/frecuencia)</b></td>
      <td>Casi siempre</td>
      <td>Alta</td>
      <td>Casi siempre</td>
      <td>Alta</td>
    </tr>
    <tr>
      <td><b>Generar proyecciones de compra</b></td>
      <td>Nunca</td>
      <td>Baja</td>
      <td>Casi siempre</td>
      <td>Muy alta</td>
    </tr>
  </tbody>
</table>

El análisis de la matriz de tareas evidencia una clara diferencia en las prioridades operativas y patrones de uso entre ambos perfiles de usuario.

En el caso de José Jiménez, quien representa al público de adultos jóvenes con agendas ajustadas, el valor principal radica en la supervisión rápida de la frescura y la recepción de avisos de caducidad; ambas funcionalidades le resultan esenciales para evitar el desperdicio de comida y proteger su economía personal. Otras herramientas, como el catálogo de recetas recomendadas o la difusión de logros en plataformas digitales, son utilizadas de forma secundaria sin representar un factor crítico dentro de su rutina diaria.

Por su parte, Luisa Pérez, orientada a la gestión de su negocio de comida casera, enfoca su interacción en herramientas de control riguroso, tales como el monitoreo constante del inventario, la revisión de métricas y la proyección de abastecimiento. Para su perfil, estas funciones son vitales para garantizar la calidad en sus productos finales y mitigar las mermas de insumos. Por el contrario, la búsqueda de recetas o funciones lúdicas resulta poco relevante para sus objetivos comerciales.


### 2.3.3. User Journey Mapping

**Segmento 1: Adultos Jóvenes**

A través de este mapa de viaje se analiza el flujo de interacción que siguen los usuarios del primer segmento al administrar sus insumos del hogar y prevenir el desperdicio desde sus propios hábitos diarios. Este grupo incluye a personas con agendas apretadas que descuidan el control constante del refrigerador, lo que genera el descarte involuntario de comida descompuesta. Por ello, buscan alternativas tecnológicas intuitivas y eficientes que les ofrezcan avisos automáticos, sugerencias de platillos sencillos y una gestión del inventario ágil que no exija esfuerzo extra.

![José Segmento 1 Journey Map](assets/Jose_Segmento1_Map.png)

**Segmento 2: Pequeños Negocios y Emprendedores de Alimentos**

El presente mapa refleja la secuencia de pasos que efectúan los usuarios del segundo segmento con el fin de supervisar sus materias primas y garantizar insumos óptimos a sus consumidores. Este perfil engloba a emprendimientos gastronómicos del hogar que experimentan merma financiera ante el vencimiento de sus ingredientes por llevar un registro manual. Priorizan sistemas que sistematicen la medición de frescura, emitan análisis de stock e indicadores de reabastecimiento, ayudando a sostener el estándar de sus entregas y la lealtad comercial de sus clientes.

![Luisa Segmento 2 Journey Map](assets/Luisa_Segmento2_Map.png)


### 2.3.4. Empathy Mapping

**Segmento 1: Adultos Jóvenes**

El esquema de empatía enfocado en José ilustra el perfil de un joven profesional con tiempo limitado que requiere automatizar el seguimiento de su comida para disminuir gastos e ineficiencias. Experimenta insatisfacción cuando se estropean sus productos y busca herramientas digitales ágiles que faciliten la planeación de sus compras e incentiven hábitos de consumo responsables.

![Empathy Map Segmento 1](assets/Empathymap_Segmento1.png)

**Segmento 2: Pequeños Negocios y Emprendedores de Alimentos**

El mapa de empatía representativo de Luisa sintetiza la perspectiva de una emprendedora comprometida con mantener la calidad de sus insumos y resguardar el prestigio de su marca. Requiere una plataforma accesible que aminore la merma económica, simplifique la organización del almacenamiento y consolide el respaldo de su clientela.

![Empathy Map Segmento 2](assets/Empathymap_Segmento2.png)


## 2.4. Big Picture EventStorming

Con la finalidad de estructurar una solución integral y alineada a las dinámicas del negocio, el equipo llevó a cabo una sesión colaborativa de EventStorming para mapear el flujo de eventos del sistema:

![event storming1](assets/Event1.PNG)
![event storming2](assets/Event2.PNG)
![event storming3](assets/Event3.PNG)
![event storming4](assets/Event4.PNG)
![event storming5](assets/Event5.jpeg)
![event storming6](assets/Event6.jpeg)
![event storming7](assets/Event7.jpeg)
![event storming8](assets/Event8.jpeg)
![event storming9](assets/Event9.jpeg)
![event storming10](assets/Event10.jpeg)


## 2.5. Ubiquitous Language

| Ubiquitous Term       | Definition of Functional Domain                                                                                                       | 
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Food Waste            | Loss or discard of edible food that could have been consumed, caused by poor management, lack of monitoring, or premature spoilage. |
| FreshSense Device     | Sensor-based hardware placed inside the refrigerator to monitor food conditions such as temperature, humidity, and ethylene gas levels. |
| Ethylene Gas          | Natural plant hormone released by fruits and vegetables during ripening, used by the system as a critical freshness indicator.       |
| Food Inventory        | Organized list and status of available food items stored at home or in small businesses, including expiration estimation.            |
| Food Condition        | Physical state of stored food determined by FreshSense (fresh, at risk, or spoiled).                                                  |
| Expiration Alert      | Notification sent to users when a food item is approaching spoilage or entering a decomposition phase.                              |
| Recipe Suggestion     | Cooking recommendation proposed by the platform, prioritizing ingredients close to expiration to prevent waste.                       |
| Consumption Report    | Periodic summary of food consumed or discarded, estimating financial impact and carbon footprint reduction.                            |
| Premium Subscription  | Paid plan unlocking advanced features such as detailed inventory analytics, exclusive recipes, and environmental statistics.         |
| Household User        | Individual or family that uses FreshSense to manage their daily food items and optimize their household budget.                        |
| Food Entrepreneur     | Small business owner who uses FreshSense to guarantee the freshness of their ingredients and reduce losses.                           |
| Sustainability Impact | Positive ecological and economic effect of reducing food waste, measured in money saved and CO₂ emissions avoided.                   |
| Gamification          | Use of challenges, badges, and achievements within the app to motivate users to actively reduce waste.                               |
| Food Monitoring       | Continuous tracking of storage conditions and freshness status of stored food products.                                                |
| Smart Notification    | Customizable alert system that tailors reminders according to user preferences to prevent invasive notifications.                   |
| Recipe Filter         | Navigation option that allows users to categorize recipes by time, difficulty level, or dietary restrictions.                          |

# Capítulo III: Requirements Specification

## 3.1. User Stories

| User Story ID | Título | Descripción | Criterios de Aceptación (Gherkin) | Relacionado con (Epic) |
| :--- | :--- | :--- | :--- | :--- |
| **US01** | Visualización de propuesta | Como potencial usuario doméstico, deseo comprender la propuesta de valor de FreshSense al ingresar al portal para evaluar sus beneficios. | **Escenario 1: Carga limpia y mensaje claro**<br>Dado que un visitante navega a la página web<br>Cuando la plataforma cargue completamente<br>Entonces se desplegará el mensaje central de valor y los módulos de solución de manera visible. | **EP01** (Landing Page) |
| **US02** | Sección para pequeñas empresas | Como emprendedor del sector alimentario, requiero información enfocada en mi rubro para entender el retorno de inversión y las ventajas operativas. | **Escenario 1: Navegación por perfil comercial**<br>Dado que un emprendedor interactúa con la landing page<br>Cuando acceda a la pestaña corporativa<br>Entonces visualizará los módulos dedicados a mermas, control de calidad y planes B2B. | **EP01** (Landing Page) |
| **US03** | Formulario de contacto y demos | Como visitante interesado, quiero enviar una solicitud de contacto de forma ágil para resolver dudas o agendar una demostración. | **Escenario 1: Envío exitoso de consulta**<br>Dado que el visitante llena sus datos de contacto válidos<br>Cuando presione el botón de envío<br>Entonces el sistema registrará la solicitud y mostrará un mensaje de confirmación en pantalla. | **EP01** (Landing Page) |
| **US04** | Call to Action (CTA) | Como cliente potencial, deseo disponer de un botón de acción visible para registrarme rápidamente o activar la prueba gratuita. | **Escenario 1: Redirección desde el CTA**<br>Dado que el usuario explora la sección de planes<br>Cuando haga clic en "Iniciar prueba gratuita"<br>Entonces será redirigido inmediatamente al formulario de registro. | **EP01** (Landing Page) |
| **US05** | Adaptabilidad en dispositivos móviles | Como usuario en movimiento, quiero navegar por la web desde cualquier teléfono o tablet sin distorsión de contenido. | **Escenario 1: Renders responsivos**<br>Dado que el visitante ingresa mediante un navegador móvil<br>Cuando explore las secciones<br>Entonces la interfaz ajustará dinámicamente sus márgenes, botones y tipografías. | **EP01** (Landing Page) |
| **US06** | Telemetría y monitoreo IoT | Como usuario del hogar, necesito que el sensor recolecte métricas de temperatura, humedad y gas etileno para prevenir el deterioro de mi comida. | **Escenario 1: Transmisión continua de telemetría**<br>Dado que el dispositivo FreshSense está en línea<br>Cuando detecte un cambio en las condiciones del ambiente<br>Entonces enviará los datos a la app en tiempo real para actualizar el panel de control.<br><br>**Escenario 2: Notificación por desconexión**<br>Dado que el sensor pierda enlace con la red Wi-Fi<br>Cuando el servidor detecte la falta de ping<br>Entonces notificará al usuario sobre el fallo de señal. | **EP02** (Monitoreo IoT) |
| **US07** | Dashboard de inventario con semáforo | Como usuario, quiero supervisar el estado de mis alimentos mediante un código de colores para identificar el riesgo de caducidad. | **Escenario 1: Vista por código de colores**<br>Dado que el usuario consulta su inventario<br>Cuando la interfaz procese la lectura de los sensores<br>Entonces catalogará cada insumo en verde (óptimo), amarillo (consumir pronto) o rojo (crítico).<br><br>**Escenario 2: Inspección detallada del producto**<br>Dado que el usuario haga clic en un insumo<br>Cuando se abra la tarjeta del alimento<br>Entonces mostrará la fecha estimada de vencimiento y los niveles actuales de etileno. | **EP02** (Monitoreo IoT) |
| **US08** | Sistema de alertas preventivas | Como usuario, requiero notificaciones oportunas cuando un alimento esté cerca de descomponerse para consumirlo a tiempo. | **Escenario 1: Notificación de riesgo**<br>Dado que un insumo pase a estado crítico<br>Cuando el motor de reglas procese los datos<br>Entonces enviará una alerta push al teléfono del cliente.<br><br>**Escenario 2: Ausencia de falsas alarmas**<br>Dado que no existan desviaciones en los parámetros<br>Cuando el sistema realice el chequeo periódico<br>Entonces no emitirá ninguna notificación innecesaria. | **EP03** (Alertas Inteligentes) |
| **US09** | Preferencias de notificaciones | Como usuario, deseo parametrizar el horario y tipo de alertas para evitar interrupciones molestas durante mi jornada. | **Escenario 1: Ajuste de horas de silencio**<br>Dado que el usuario defina un rango de quietud (ej. 22:00 a 07:00)<br>Cuando se active una alerta de baja severidad<br>Entonces la app la retendrá hasta que finalice el periodo configurado. | **EP03** (Alertas Inteligentes) |
| **US10** | Alta de productos por voz y QR | Como usuario con poco tiempo, quiero agregar insumos al inventario mediante comandos de voz o escaneo de código de barras para ahorrar esfuerzo. | **Escenario 1: Registro por comando de voz**<br>Dado que el usuario dicte "Agregar 1 kilo de manzanas"<br>Cuando la voz sea procesada por el motor de PLN<br>Entonces el insumo aparecerá registrado en la despensa virtual.<br><br>**Escenario 2: Alta rápida mediante código de barras**<br>Dado que el usuario escanee el empaque de un producto<br>Cuando la app identifique el código en la base de datos<br>Entonces completará de forma automática el nombre y la categoría. | **EP04** (Gestión de Inventario) |
| **US11** | Modificación manual de despensa | Como usuario, quiero corregir o actualizar las cantidades de mi inventario manualmente para mantener el registro alineado con la realidad. | **Escenario 1: Actualización de stock**<br>Dado que el usuario reduzca las unidades de un producto<br>Cuando guarde la modificación<br>Entonces el sistema reajustará el porcentaje restante del artículo. | **EP04** (Gestión de Inventario) |
| **US12** | Reporte semanal de hábitos | Como usuario, requiero un informe periódico de consumo y mermas para evaluar mi progreso en la reducción de desperdicio. | **Escenario 1: Emisión de reporte semanal**<br>Dado que se cumpla el ciclo de 7 días<br>Cuando el servidor consolide los datos de uso<br>Entonces enviará un resumen gráfico al correo registrado y al panel principal. | **EP04** (Gestión de Inventario) |
| **US13** | Recomendación de recetas inteligentes | Como usuario, quiero recibir sugerencias de platillos basadas en ingredientes prontos a vencer para aprovecharlos. | **Escenario 1: Generación de platillos por prioridad**<br>Dado que existan insumos en alerta amarilla o roja<br>Cuando el usuario ingrese a la pestaña de cocina<br>Entonces el motor propondrá recetas que utilicen como base dichos productos. | **EP05** (Recetas Personalizadas) |
| **US14** | Filtrado avanzado de platillos | Como usuario con restricciones alimentarias, quiero filtrar recetas por tiempo, dificultad o tipo de dieta (vegana, keto, etc.). | **Escenario 1: Aplicación de filtros combinados**<br>Dado que el usuario seleccione "Fácil", "< 20 min" y "Vegetariano"<br>Cuando ejecute la búsqueda<br>Entonces el catálogo desplegará únicamente las opciones que satisfagan todos los criterios. | **EP05** (Recetas Personalizadas) |
| **US15** | Onboarding y tutorial interactivo | Como cliente nuevo, deseo contar con una guía interactiva al iniciar sesión por primera vez para aprender a utilizar las funciones clave. | **Escenario 1: Módulo de aprendizaje inicial**<br>Dado que un usuario inicie sesión por primera vez<br>Cuando se abra la pantalla de bienvenida<br>Entonces se desplegará un tour paso a paso con la explicación de las herramientas. | **EP06** (UX y Accesibilidad) |
| **US16** | Interfaz amigable e inclusiva | Como usuario, quiero disponer de una aplicación limpia, legible y con contraste adecuado para navegar de forma cómoda. | **Escenario 1: Navegación accesible**<br>Dado que el usuario explore el tablero principal<br>Cuando interactúe con las tarjetas e íconos<br>Entonces la interfaz responderá de manera fluida y adaptada a estándares WCAG AA. | **EP06** (UX y Accesibilidad) |
| **US17** | Analítica avanzada de inventario | Como usuario premium, deseo visualizar gráficos detallados de la velocidad de rotación de mi comida para optimizar compras futuras. | **Escenario 1: Acceso a métricas corporativas**<br>Dado un usuario con plan activo Premium<br>Cuando acceda al menú de analítica<br>Entonces podrá inspeccionar gráficos comparativos de entradas, consumo y merma por periodos. | **EP07** (Suscripción Premium) |
| **US18** | Panel de ahorro financiero | Como cliente suscrito, quiero evaluar el dinero que he dejado de perder al consumir alimentos a tiempo. | **Escenario 1: Cálculo de ahorro acumulado**<br>Dado que el sistema registre alimentos consumidos antes del vencimiento<br>Cuando el usuario consulte su perfil<br>Entonces visualizará una estimación en moneda local del valor rescatado. | **EP07** (Suscripción Premium) |
| **US19** | Catálogo de recetas gourmet | Como usuario abonado a la suscripción, quiero acceder a preparaciones exclusivas diseñadas por chefs para variar mi dieta. | **Escenario 1: Desbloqueo de contenido exclusivo**<br>Dado un usuario de nivel Premium<br>Cuando consulte la sección de recetas avanzadas<br>Entonces dispondrá de acceso ilimitado a videoguías y listas de ingredientes paso a paso. | **EP07** (Suscripción Premium) |
| **US20** | Métricas de impacto ecológico | Como usuario comprometido con el medio ambiente, quiero revisar la reducción de mi huella de carbono derivada de evitar desperdicios. | **Escenario 1: Estimación de CO₂ evitado**<br>Dado el registro de comida salvada durante el mes<br>Cuando el usuario visite la pestaña de sostenibilidad<br>Entonces la app mostrará la equivalencia en kilogramos de CO₂ y litros de agua preservados. | **EP08** (Sostenibilidad) |
| **US21** | Integración y difusión en redes | Como usuario orgullo de sus avances, quiero compartir mis insignias y logros ecológicos en redes sociales para motivar a mis contactos. | **Escenario 1: Publicación de tarjeta de logro**<br>Dado que el usuario alcance una meta mensual<br>Cuando haga clic en "Compartir en redes"<br>Entonces la plataforma generará una imagen personalizada lista para subir a sus historias. | **EP08** (Sostenibilidad) |
| **US22** | Sincronización con refrigeradores inteligentes | Como usuario con electrodomésticos IoT, quiero enlazar FreshSense con mi heladera inteligente para unificar las lecturas. | **Escenario 1: Mapeo de sensores externos**<br>Dado un refrigerador inteligente compatible<br>Cuando se complete el emparejamiento mediante API<br>Entonces la app consolidará la información interna del electrodoméstico con la del sensor FreshSense. | **EP09** (Integración IoT) |
| **US23** | Comandos de voz mediante asistentes | Como usuario, quiero consultar el estado de mi heladera usando Alexa o Google Assistant mientras cocino. | **Escenario 1: Consulta verbal de inventario**<br>Dado que la skill esté vinculada con el asistente de voz<br>Cuando el usuario pregunte "¿Qué alimentos están por vencer?"<br>Entonces el asistente responderá leyendo los artículos en alerta amarilla y roja. | **EP09** (Integración IoT) |
| **US24** | Ruteo de notificaciones multidispositivo | Como usuario con múltiples dispositivos, quiero seleccionar en qué equipo (reloj, celular, correo) recibir cada tipo de aviso. | **Escenario 1: Ruteo preferencial**<br>Dado que el usuario seleccione recibir avisos críticos en su Smartwatch<br>Cuando se dispare una alerta roja<br>Entonces el servidor la desviará inmediatamente al canal de reloj inteligente. | **EP09** (Integración IoT) |
| **US25** | Gamificación y medallas | Como usuario, quiero obtener puntos e insignias por registrar mi comida y evitar mermas para mantener la motivación. | **Escenario 1: Adjudicación de insignias**<br>Dado que el usuario pase 14 días sin desechar alimentos<br>Cuando el sistema verifique el registro<br>Entonces le otorgará la medalla "Héroe del Ahorro" y sumará puntos a su cuenta. | **EP10** (Gamificación) |
| **US26** | Módulo de interacción social | Como usuario activo, quiero interactuar con comunidades de consumo responsable para intercambiar recetas y consejos de conservación. | **Escenario 1: Publicación en el foro comunitario**<br>Dado que el usuario ingrese al muro social<br>Cuando publique un consejo de almacenamiento<br>Entonces otros usuarios podrán reaccionar y guardar el tip en sus favoritos. | **EP10** (Gamificación) |
| **US27** | Desafíos y rankings comunitarios | Como usuario competitivo, quiero participar en retos mensuales entre usuarios para ver quién disminuye más su desperdicio. | **Escenario 1: Posicionamiento en tabla de líderes**<br>Dado que un reto mensual esté activo<br>Cuando el usuario registre reducciones en mermas<br>Entonces su posición escalará en la tabla pública de clasificación. | **EP10** (Gamificación) |
| **US28** | Categorización personalizada de insumos | Como usuario organizado, quiero crear etiquetas a medida (ej. "Insumos de Repostería", "Bebidas") para ordenar mi despacho. | **Escenario 1: Creación de etiquetas custom**<br>Dado que el usuario agregue la categoría "Congelados Especiales"<br>Cuando categorice nuevos artículos<br>Entonces podrá filtrar la vista del inventario bajo ese grupo recién creado. | **EP11** (Gestión Avanzada) |
| **US29** | Historial de consumo exportable | Como administrador de despensa, quiero consultar y descargar la lista histórica de lo consumido y desechado para ajustar mis presupuestos. | **Escenario 1: Exportación de archivo de datos**<br>Dado que el usuario defina un rango de fechas<br>Cuando presione "Exportar historial"<br>Entonces el sistema descargará un archivo en formato CSV o Excel con el detalle completo. | **EP11** (Gestión Avanzada) |
| **US30** | Algoritmo de sugerencias de compra | Como usuario, quiero recibir una lista sugerida de compras según mi patrón histórico de consumo para no comprar en exceso. | **Escenario 1: Generación de lista automática**<br>Dado el historial de consumo de los últimos 30 días<br>Cuando el usuario planifique su salida al supermercado<br>Entonces la app recomendará la cantidad exacta de insumos a reponer. | **EP11** (Gestión Avanzada) |
| **US31** | Vinculación y calibración de hardware | Como usuario, quiero vincular un nuevo sensor FreshSense escaneando su código QR e ingresar la temperatura base de mi refrigerador para calibrar el equipo. | **Escenario 1: Vinculación QR exitosa**<br>Dado que el usuario abre el instalador de la app<br>Cuando escanee el código QR pegado en el hardware<br>Entonces el dispositivo quedará enlazado a su hogar y listo para medir. | **EP02** (Monitoreo IoT) |
| **US32** | Modo de conservación fuera de casa | Como usuario que sale de viaje, quiero activar el "Modo Vacaciones" para recalibrar los umbrales de alerta al no abrirse la puerta del refrigerador. | **Escenario 1: Activación de modo viaje**<br>Dado que el usuario activa el interruptor "Modo Vacaciones"<br>Cuando transcurran más de 24 horas sin apertura de puerta<br>Entonces el sistema ajustará la sensibilidad de emisión de etileno para evitar alertas falsas. | **EP03** (Alertas Inteligentes) |
| **US33** | Gestión de múltiples áreas de almacenamiento | Como emprendedor de alimentos, quiero crear distintas zonas (ej. "Cámara Fría 1", "Frigorífico Verduras") para organizar mis sensores. | **Escenario 1: Asignación de ubicación**<br>Dado que el usuario crea la zona "Congelador Carnes"<br>Cuando vincule un sensor a esa zona<br>Entonces los alimentos asociados tomarán las reglas de temperatura de esa cámara específica. | **EP11** (Gestión Avanzada) |
| **US34** | Registro de causas de descarte | Como usuario o negocio, quiero registrar el motivo específico cuando tiro un alimento (ej. "Caducado", "Contaminado", "Mal estado al comprar") para entender mis mermas. | **Escenario 1: Registro de motivo de baja**<br>Dado que el usuario elimine un producto marcándolo como "Desechado"<br>Cuando la app solicite el motivo<br>Entonces guardará la causa elegida para incluirla en el informe mensual de desperdicio. | **EP04** (Gestión de Inventario) |
| **US35** | Recuperación y restablecimiento de contraseña | Como usuario registrado, quiero restablecer mi contraseña mediante un enlace seguro enviado a mi correo cuando olvide mis credenciales de acceso. | **Escenario 1: Restablecimiento por correo**<br>Dado que el usuario haga clic en "¿Olvidaste tu contraseña?" e ingrese su email<br>Cuando presione "Enviar enlace"<br>Entonces el sistema despachará un correo con un token único de restablecimiento temporal. | **EP12** (Core API) |
| **US36** | Panel de administración de usuarios y roles | Como administrador de FreshSense, quiero gestionar cuentas, modificar roles (Free, Premium, Admin) y suspender accesos indebidos. | **Escenario 1: Modificación de plan por administrador**<br>Dado un usuario con cuenta gratuita activa<br>Cuando el administrador actualice su rol a "Premium B2B"<br>Entonces el usuario dispondrá de acceso inmediato a los módulos de analítica avanzada. | **EP12** (Core API) |
| **US37** | Gestión de miembros del hogar/negocio | Como usuario principal, quiero invitar a otros miembros de mi familia o empleados para que gestionen el mismo inventario compartido. | **Escenario 1: Aceptación de invitación familiar**<br>Dado que el titular envíe una invitación por correo a su cónyuge<br>Cuando el invitado acepte el enlace de vinculación<br>Entonces ambos visualizarán y editarán la misma despensa en tiempo real. | **EP04** (Gestión de Inventario) |
| **US38** | Descarga de comprobantes de pago | Como suscriptor Premium, quiero descargar las facturas o boletas electrónicas de mis cobros mensuales para llevar la contabilidad de mi negocio. | **Escenario 1: Descarga de factura PDF**<br>Dado que el cobro mensual de la suscripción haya sido procesado<br>Cuando el usuario acceda a la sección "Historial de Pagos"<br>Entonces podrá descargar el comprobante en formato PDF. | **EP07** (Suscripción Premium) |
| **US39** | Búsqueda global con autocompletado | Como usuario con un inventario extenso, quiero buscar cualquier alimento o receta escribiendo en una barra de búsqueda con sugerencias en vivo. | **Escenario 1: Búsqueda dinámica**<br>Dado que el usuario escriba "Manz" en el buscador principal<br>Cuando el sistema procese el texto<br>Entonces desplegará en tiempo real los artículos coincidentes del inventario y recetas sugeridas. | **EP06** (UX y Accesibilidad) |
| **US40** | Calificación y reseñas de recetas | Como usuario cocinero, quiero calificar con estrellas y comentar las recetas sugeridas para ayudar a la comunidad a elegir las mejores opciones. | **Escenario 1: Publicación de calificación**<br>Dado que el usuario prepare un plato recomendado<br>Cuando asigne 5 estrellas y escriba una reseña<br>Entonces su comentario se actualizará inmediatamente en la ficha pública de la receta. | **EP05** (Recetas Personalizadas) |
| **TS41** | API Ingesta de Sensores IoT | Como desarrollador Backend, requiero un endpoint RESTful seguro de alta velocidad para almacenar las lecturas de los microcontroladores. | **Escenario 1: Persistencia exitosa de telemetría**<br>Dado que un sensor autenticado envíe un JSON con lecturas de etileno, humedad y temperatura<br>Cuando el backend valide el token de acceso<br>Entonces almacenará los registros en la base de datos y responderá un código HTTP 201. | **EP12** (Core API) |
| **TS42** | Microservicio de Notificaciones | Como desarrollador Backend, necesito un módulo independiente para la gestión y despacho de avisos push y correos electrónicos. | **Escenario 1: Despacho asíncrono de alertas**<br>Dado un evento de alimento en peligro<br>Cuando el microservicio reciba el mensaje de la cola de eventos<br>Then procesará la plantilla correspondiente y la despachará hacia el proveedor de notificaciones (Firebase/SendGrid). | **EP12** (Core API) |
| **TS43** | API Gestor de Autenticación y RBAC | Como desarrollador Backend, preciso implementar un control de acceso basado en roles (RBAC) con tokens JWT para proteger las funciones Premium. | **Escenario 1: Validación de permisos por rol**<br>Dado que un usuario sin suscripción intente consumir un endpoint exclusivo<br>Cuando el middleware de autenticación analice el JWT<br>Entonces bloqueará el paso devolviendo un estado HTTP 403 Forbidden. | **EP12** (Core API) |
| **TS44** | Integración de Pasarela de Pagos Stripe/PayPal | Como desarrollador Backend, necesito integrar los webhooks de cobro recurrente para automatizar la activación y cancelación de suscripciones Premium. | **Escenario 1: Confirmación de pago por Webhook**<br>Dado que la pasarela de pagos procese exitosamente la renovación mensual<br>Cuando el servidor reciba la notificación del Webhook<br>Entonces extenderá automáticamente la fecha de vigencia del usuario por 30 días más. | **EP07** (Suscripción Premium) |
| **TS45** | Sistema de Caching de Recetas y Consultas Frecuentes | Como desarrollador Backend, necesito implementar una capa de caché con Redis para optimizar el tiempo de respuesta del catálogo de recetas. | **Escenario 1: Respuesta desde la memoria caché**<br>Dado que una consulta de recetas filtradas haya sido realizada previamente<br>Cuando un nuevo usuario ejecute el mismo filtro<br>Entonces la API servirá la información desde Redis reduciendo el tiempo de respuesta a menos de 50ms. | **EP12** (Core API) |
## Epics (Épicas)

| Epic ID | Título de la Épica | Alcance y Descripción Corta |
| :--- | :--- | :--- |
| **EP01** | Portal Informativo y Landing Page | Estructuración y despliegue del sitio web principal enfocado en la conversión de visitantes, destacando la propuesta de valor, planes para hogares y pymes, secciones educativas y captura de leads. |
| **EP02** | Telemetría e Ingesta IoT | Desarrollo del sistema continuo de captura, calibración y procesamiento en tiempo real de las lecturas físicas (temperatura, porcentaje de humedad y niveles de gas etileno) enviadas por el hardware FreshSense. |
| **EP03** | Motor de Alertas e Indicadores de Riesgo | Algoritmo inteligente encargado de evaluar las desviaciones métricas frente a los umbrales de seguridad, gestionando notificaciones preventivas y modos especiales de conservación (ej. Modo Vacaciones). |
| **EP04** | Gestión Dinámica de Inventario y Despensa | Módulo para la organización integral de insumos, incluyendo altas por comandos de voz o escaneo de código de barras, actualizaciones manuales, clasificación por despensas y control de miembros del hogar. |
| **EP05** | Motor de Sugerencia de Recetas | Sistema dinámico que analiza los ingredientes próximos a vencer en el refrigerador y propone recetas personalizadas, filtrables por tipo de dieta, tiempo de preparación e interacciones comunitarias. |
| **EP06** | Experiencia de Usuario, Accesibilidad y Navegación | Diseño UX/UI intuitivo y accesible bajo estándares WCAG AA, que contempla búsquedas globales con autocompletado, vistas responsivas en múltiples pantallas y módulos de onboarding guiado para nuevos usuarios. |
| **EP07** | Modelo de Suscripción y Pasarela de Pagos | Módulo de monetización encargado del cobro recurrente mediante webhooks (Stripe/PayPal), la descarga de comprobantes electrónicos de pago y el desbloqueo de capacidades exclusivas Premium. |
| **EP08** | Analítica de Sostenibilidad e Impacto Ambiental | Sistema de cálculo enfocado en cuantificar el volumen de comida salvada, la reducción estimada de la huella de carbono (kg de CO₂ evitado), el consumo de agua preservado y su difusión en redes sociales. |
| **EP09** | Conectividad y Ecosistemas Smart | Módulos de expansión para la integración con electrodomésticos IoT (Smart Fridges), asistentes virtuales de voz (Alexa/Google Assistant) y ruteo de notificaciones hacia relojes inteligentes. |
| **EP10** | Gamificación, Desafíos y Comunidad | Funcionalidades de interacción social que incentivan el consumo responsable mediante el otorgamiento de insignias, puntos por metas cumplidas, foros comunitarios y tablas de posición en retos mensuales. |
| **EP11** | Analítica Comercial y Gestión Avanzada B2B | Herramientas orientadas a emprendedores y pymes para la organización por cámaras frías, registro de causas de descarte, exportación de reportes financieros en Excel/PDF y algoritmos proyectivos de reabastecimiento. |
| **EP12** | Arquitectura Backend, Seguridad y Core API | Construcción de la base del servidor, microservicios de despacho asíncrono de avisos, capa de almacenamiento en caché con Redis, recuperación de credenciales y control de acceso basado en roles (RBAC JWT). |

## 3.2. Impact Mapping

![impact mapping](assets/ImpactMap_FreshSense.PNG)

En conclusión, el Impact Mapping permitió establecer una trazabilidad nítida entre la visión de negocio y la implementación del software. Esto garantiza que cada desarrollo atienda un requisito técnico y genere una transformación medible en los hábitos de uso, disminuyendo el desperdicio alimentario y acelerando el crecimiento de FreshSense.

---

## 3.3. Product Backlog

A continuación se presenta el **Product Backlog** priorizado del proyecto FreshSense, estimando el esfuerzo en Story Points mediante la escala de Fibonacci (1, 2, 3, 5, 8) e integrando la totalidad de las 45 historias definidas:

| Orden (#) | User Story ID | Título de la Historia / Tarea Técnica | Descripción Sintetizada | Story Points |
| :-: | :--- | :--- | :--- | :-: |
| **1** | **US01** | Visualización de propuesta de valor | Explicación clara de la propuesta de FreshSense en la landing page para visitantes. | **2** |
| **2** | **US02** | Sección para pequeños negocios | Módulo web orientado a emprendedores gastronómicos para destacar ventajas comerciales. | **2** |
| **3** | **US03** | Formulario de contacto y demos | Formulario dinámico para la recepción de solicitudes de información y demostraciones. | **2** |
| **4** | **US04** | Call to Action (CTA) | Botón de llamado a la acción para la conversión rápida hacia el registro o prueba gratis. | **2** |
| **5** | **US05** | Adaptabilidad en móviles | Configuración de estilos responsivos para asegurar una lectura cómoda en celulares. | **3** |
| **6** | **TS43** | API Gestor de Autenticación y RBAC | Configuración del servidor de identidad con seguridad basada en tokens JWT y permisos. | **5** |
| **7** | **TS41** | API Ingesta de Sensores IoT | Endpoint RESTful encargado de recibir y almacenar datos de etileno, humedad y temperatura. | **5** |
| **8** | **US06** | Telemetría y monitoreo IoT | Recolección en tiempo real de métricas enviadas por los sensores FreshSense. | **5** |
| **9** | **US07** | Dashboard con semáforo | Módulo visual que clasifica la frescura de la comida mediante colores verde, amarillo y rojo. | **3** |
| **10** | **US08** | Sistema de alertas preventivas | Notificaciones automáticas ante el riesgo inminente de caducidad en un insumo. | **5** |
| **11** | **TS42** | Microservicio de Notificaciones | Módulo asíncrono para la emisión de avisos push hacia móviles y correo electrónico. | **3** |
| **12** | **US09** | Preferencias de notificaciones | Panel para parametrizar horarios de silencio y canales de contacto preferidos. | **3** |
| **13** | **US31** | Vinculación y calibración de hardware | Módulo de emparejamiento de sensores mediante código QR y calibración de temperatura. | **3** |
| **14** | **US10** | Alta de productos por voz y QR | Registro rápido de ingredientes escaneando códigos de barra o mediante comandos de voz. | **5** |
| **15** | **US11** | Modificación manual de despensa | Edición de cantidades, nombres y categorías dentro de la despensa digital. | **2** |
| **16** | **US37** | Gestión de miembros del hogar/negocio | Invitación y vinculación de familiares o empleados a un mismo inventario compartido. | **3** |
| **17** | **US12** | Reporte semanal de hábitos | Consolidado periódico que detalla el volumen de insumos consumidos y descartados. | **3** |
| **18** | **US13** | Recomendación de recetas inteligentes | Algoritmo que sugiere platillos basándose en los ingredientes próximos a vencer. | **5** |
| **19** | **US14** | Filtrado avanzado de platillos | Selección de recetas por tiempo de preparación, grado de dificultad y tipo de dieta. | **3** |
| **20** | **US39** | Búsqueda global con autocompletado | Barra de búsqueda centralizada para filtrar insumos y recetas con sugerencias en vivo. | **3** |
| **21** | **US15** | Onboarding y tutorial interactivo | Tour interactivo para guiar la primera experiencia del usuario en la plataforma. | **2** |
| **22** | **US16** | Interfaz amigable e inclusiva | Optimización UX/UI para asegurar altos estándares de legibilidad y accesibilidad. | **3** |
| **23** | **TS44** | Pasarela de Pagos Recurrentes | Integración de webhooks para cobros periódicos de membresías Premium (Stripe/PayPal). | **5** |
| **24** | **US17** | Analítica avanzada de inventario | Dashboard con gráficos de rotación de stock exclusivo para cuentas Premium. | **5** |
| **25** | **US18** | Panel de ahorro financiero | Métricas que cuantifican en moneda local el valor rescatado del desperdicio. | **3** |
| **26** | **US19** | Catálogo de recetas gourmet | Sección de contenido culinario exclusivo y videoguías para suscriptores abonados. | **2** |
| **27** | **US38** | Descarga de comprobantes de pago | Módulo de consulta y descarga de facturas/boletas electrónicas en formato PDF. | **2** |
| **28** | **US20** | Métricas de impacto ecológico | Estimación del equivalente en CO₂ evitado y recursos naturales preservados. | **3** |
| **29** | **US21** | Integración y difusión en redes | Generador de tarjetas visuales de logros para compartir avances en canales sociales. | **2** |
| **30** | **US32** | Modo de conservación fuera de casa | Calibración especial de umbrales para periodos largos sin apertura de puerta (Modo Vacaciones). | **2** |
| **31** | **US33** | Gestión de áreas de almacenamiento | Configuración de múltiples frigoríficos o cámaras frías dentro de un mismo negocio. | **3** |
| **32** | **US34** | Registro de causas de descarte | Clasificación de motivos de baja (caducidad, contaminación) para afinar métricas de merma. | **2** |
| **33** | **US28** | Categorización personalizada | Creación de etiquetas custom para agrupar inventarios según preferencias del usuario. | **3** |
| **34** | **US29** | Historial de consumo exportable | Funcionalidad para descargar informes detallados de consumo en formatos CSV y Excel. | **5** |
| **35** | **US30** | Algoritmo de sugerencias de compra | Proyección automatizada de compras para reponer insumos evitando compras excesivas. | **5** |
| **36** | **US25** | Gamificación y medallas | Otorgamiento automático de insignias y puntos tras cumplir metas sostenibles. | **3** |
| **37** | **US26** | Módulo de interacción social | Espacio de comunidad para intercambiar recomendaciones y recetas de aprovechamiento. | **2** |
| **38** | **US27** | Desafíos y rankings comunitarios | Tabla competitiva mensual entre usuarios para incentivar la reducción de desperdicio. | **5** |
| **39** | **US40** | Calificación y reseñas de recetas | Sistema de valoración con estrellas y comentarios para calificar preparaciones. | **2** |
| **40** | **US35** | Recuperación de contraseña | Flujo seguro de restablecimiento de clave vía enlace temporal enviado por correo. | **2** |
| **41** | **US36** | Panel de administración de usuarios | Módulo interno para la supervisión de cuentas, gestión de roles y suspensión de accesos. | **3** |
| **42** | **US24** | Ruteo de notificaciones multidispositivo | Enrutamiento de alertas hacia dispositivos específicos (relojes inteligentes, móviles). | **3** |
| **43** | **TS45** | Caching de Consultas Frecuentes | Capa de almacenamiento en memoria con Redis para servir catálogos en menos de 50ms. | **3** |
| **44** | **US22** | Sincronización con smart fridges | Enlace e integración API directa con refrigeradores inteligentes compatibles. | **8** |
| **45** | **US23** | Comandos de voz mediante asistentes | Desarrollo de skill para consultar el inventario mediante Alexa o Google Assistant. | **5** |

Capítulo IV: Solution Software Design

4.1. Strategic-Level Domain-Driven Design.

4.1.1. Design-Level EventStorming.

4.1.1.1 Candidate Context Discovery.

4.1.1.2 Domain Message Flows Modeling.

4.1.1.3 Bounded Context Canvases.

4.1.2. Context Mapping.

4.1.3. Software Architecture.

4.1.3.1. Software Architecture System Landscape Diagram.

4.1.3.2. Software Architecture Context Level Diagrams.

4.1.3.2. Software Architecture Container Level Diagrams.

4.1.3.3. Software Architecture Deployment Diagrams.

4.2. Tactical-Level Domain-Driven Design

4.2.X. Bounded Context: <Bounded Context Name>

4.2.X.1. Domain Layer.

4.2.X.2. Interface Layer.

4.2.X.3. Application Layer.

4.2.X.4. Infrastructure Layer.

4.2.X.5. Bounded Context Software Architecture Component Level Diagrams.

4.2.X.6. Bounded Context Software Architecture Code Level Diagrams.

4.2.X.6.1. Bounded Context Domain Layer Class Diagrams.

4.2.X.6.2. Bounded Context Database Design Diagram.

Capítulo V: Solution UI/UX Design

5.1. Style Guidelines.

5.1.1. General Style Guidelines.

5.1.2. Web, Mobile and IoT Style Guidelines.

5.2. Information Architecture.

5.2.1. Organization Systems.

5.2.2. Labeling Systems.

5.2.3. SEO Tags and Meta Tags

5.2.4. Searching Systems.

5.2.5. Navigation Systems.

5.3. Landing Page UI Design.

5.3.1. Landing Page Wireframe.

5.3.2. Landing Page Mock-up.

5.4. Applications UX/UI Design.

5.4.1. Applications Wireframes.

5.4.2. Applications Wireflow Diagrams.

5.4.2. Applications Mock-ups.

5.4.3. Applications User Flow Diagrams.

5.5. Applications Prototyping.

5.6. IoT Device Design.

Capítulo VI: Product Implementation, Validation & Deployment

6.1. Software Configuration Management.

6.1.1. Software Development Environment Configuration.

6.1.2. Source Code Management.

6.1.3. Source Code Style Guide & Conventions.

6.1.4. Software Deployment Configuration.

6.2. Landing Page, Services & Applications Implementation.

6.2.X. Sprint n

6.2.X.1. Sprint Planning n.

6.2.X.2. Aspect Leaders and Collaborators.

6.2.X.3. Sprint Backlog n.

6.2.X.4. Development Evidence for Sprint Review.

6.2.X.5. Testing Suite Evidence for Sprint Review.

6.2.X.6. Execution Evidence for Sprint Review.

6.2.X.7. Services Documentation Evidence for Sprint Review.

6.2.X.8. Software Deployment Evidence for Sprint Review.

6.2.X.9. Team Collaboration Insights during Sprint.

6.3. Validation Interviews.

6.3.1. Diseño de Entrevistas.

6.3.2. Registro de Entrevistas.

6.3.3. Evaluaciones según heurísticas.

6.4. Video About-the-Product.

Conclusiones

Conclusiones y recomendaciones.

Video About-the-Team.
Bibliografía
Anexos
