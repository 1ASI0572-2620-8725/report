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

# Capítulo II: Requirements Elicitation & Analysis

## 2.1. Competidores

El análisis de competidores de FreshSense se enfoca en soluciones empresariales relacionadas con monitoreo de cadena de frío, control de condiciones ambientales, trazabilidad y supervisión de productos sensibles a la temperatura.

Debido al enfoque actual de FreshSense hacia empresas de distribución y cadena de frío, así como empresas productoras y comercializadoras de alimentos perecibles, se seleccionaron tres competidores directos que ofrecen soluciones basadas en dispositivos IoT y plataformas digitales para el monitoreo de productos durante almacenamiento o transporte:

- **Sensitech**
- **Tive**
- **Roambee**

Estas soluciones presentan similitudes con FreshSense en el monitoreo de variables ambientales, generación de alertas y visualización de información en plataformas digitales. Sin embargo, se diferencian en su nivel de especialización, mercados atendidos, alcance internacional y complejidad tecnológica.

### 2.1.1. Análisis competitivo

El objetivo de este análisis es responder la siguiente pregunta:

> **¿Cómo puede FreshSense diferenciarse de las soluciones empresariales existentes de monitoreo de cadena de frío mediante una propuesta enfocada en alimentos perecibles, facilidad de implementación y centralización de información de lotes, dispositivos y alertas?**

Los competidores seleccionados representan alternativas consolidadas dentro del mercado de monitoreo de condiciones y visibilidad de cadena de suministro.

#### Competitive Analysis Landscape

| Criterio | FreshSense | Sensitech | Tive | Roambee |
|---|---|---|---|---|
| **Tipo de competidor** | Startup analizada | Directo | Directo | Directo |
| **Overview** | Solución IoT enfocada en el monitoreo de productos perecibles mediante dispositivos que recopilan temperatura y humedad y transmiten información hacia una plataforma digital. | Empresa especializada en visibilidad y monitoreo de cadena de frío, con soluciones para almacenamiento y transporte de productos sensibles. | Plataforma de visibilidad logística en tiempo real que combina rastreadores IoT con una plataforma cloud para monitorear envíos. | Plataforma de visibilidad de cadena de suministro que combina dispositivos IoT, sensores, conectividad y análisis para monitorear mercancías y activos. |
| **Ventaja competitiva** | Propuesta enfocada específicamente en empresas que trabajan con alimentos perecibles, con una arquitectura simplificada basada en dispositivos IoT, monitoreo de lotes, alertas y trazabilidad. | Amplio portafolio especializado en cadena de frío, experiencia empresarial y soluciones para almacenamiento y transporte. | Amplia capacidad de monitoreo multimodal y dispositivos capaces de medir múltiples variables en tiempo real. | Integración de monitoreo de condiciones, ubicación, analítica y visibilidad logística en una misma plataforma. |
| **Valor ofrecido al cliente** | Centralizar información sobre condiciones de conservación, dispositivos, lotes y alertas para detectar desviaciones y reducir pérdidas por deterioro. | Proteger la integridad de productos mediante monitoreo continuo, alertas y visibilidad de extremo a extremo. | Detectar desviaciones durante el transporte en tiempo real para actuar antes de que el producto resulte comprometido. | Proporcionar información en tiempo real y señales relacionadas con condiciones y ubicación para mejorar la toma de decisiones logísticas. |
| **Mercado objetivo** | Empresas de distribución y cadena de frío; productores y comercializadores de alimentos perecibles. | Alimentos, ciencias de la vida, industria y organizaciones con cadenas de suministro sensibles a temperatura. | Alimentos y bebidas, productos perecibles, farmacéutica, ciencias de la vida, bienes de alto valor y operadores logísticos. | Empresas de logística, alimentos y bebidas, farmacéutica, manufactura y organizaciones con cadenas de suministro complejas. |
| **Estrategia de marketing** | Marketing B2B orientado a demostrar reducción de pérdidas, control de condiciones y facilidad de monitoreo. | Demostraciones comerciales, contenido especializado, casos de uso e información dirigida a industrias reguladas y cadenas de frío. | Demostraciones, pruebas de producto, contenido especializado y comunicación centrada en visibilidad logística y prevención de pérdidas. | Demostraciones, pruebas del servicio, contenido sobre supply chain y comunicación orientada a visibilidad y analítica logística. |
| **Productos y servicios** | Dispositivo IoT con ESP32 + DHT22, Edge API, plataforma Web/Mobile, monitoreo de temperatura y humedad, lotes, dispositivos, alertas, trazabilidad y reportes. | SensiWatch Platform, TempTale, ColdStream Site y distintos sensores/registradores para monitoreo estacionario y en tránsito. | Plataforma Tive, trackers Solo Lite, Solo 5G, Solo Pro, sensores, alertas, reportes e integraciones. | Plataforma de visibilidad, dispositivos como BeeSense, monitoreo de temperatura, humedad, ubicación y eventos de transporte. |
| **Precios y costos** | Modelo previsto basado en dispositivo IoT y servicio digital. Los precios comerciales deben validarse posteriormente con los segmentos objetivo. | No publica una lista estándar de precios; el acceso comercial se gestiona mediante contacto y demostración. | Los precios de los trackers principales no se publican de forma general y dependen del volumen y contrato. La plataforma dispone de niveles Essential, Plus y Premium. | Utiliza modelos de suscripción y planes bajo demanda definidos mediante órdenes comerciales según cantidad de dispositivos, activos o envíos. |
| **Canales de distribución** | Landing Page, Web Application y Mobile Application. | Plataforma web, aplicación móvil y contacto comercial. | Plataforma web, integraciones/API y soluciones de seguimiento accesibles digitalmente. | Plataforma web, aplicación móvil, API y contacto comercial. |

### Sensitech

Sensitech ofrece soluciones de monitoreo de cadena de frío tanto para productos almacenados como transportados. Su sistema de monitoreo estacionario permite controlar temperatura y humedad en almacenes e instalaciones, consultar datos históricos y en tiempo real y generar alertas cuando las condiciones salen de los rangos establecidos.

También dispone de la plataforma SensiWatch, que proporciona visibilidad de extremo a extremo de la cadena de suministro y acceso a información desde dispositivos móviles.

#### SWOT - Sensitech

**Fortalezas**

- Amplio portafolio especializado en cadena de frío.
- Monitoreo estacionario y durante transporte.
- Soporte para temperatura, humedad y otras variables.
- Alertas y datos en tiempo real.
- Experiencia en sectores como alimentos y ciencias de la vida.
- Plataforma Web y aplicación móvil.

**Debilidades**

- Solución empresarial de mayor complejidad que puede requerir procesos de implementación y contratación más extensos.
- No ofrece precios públicos estándar para sus principales soluciones.
- Su amplio alcance puede resultar superior a las necesidades de empresas que requieren únicamente monitoreo básico de alimentos perecibles.

**Oportunidades**

- Crecimiento de la digitalización en cadenas de frío.
- Mayor necesidad de trazabilidad y reducción de pérdidas de productos sensibles.
- Incremento de requisitos de control y cumplimiento en cadenas logísticas.

**Amenazas**

- Aparición de soluciones IoT de menor costo.
- Empresas que desarrollen sistemas internos utilizando sensores y plataformas cloud.
- Competidores especializados en soluciones más simples para sectores específicos.

### Tive

Tive ofrece monitoreo de cadena de frío en tiempo real utilizando dispositivos capaces de recopilar información sobre temperatura, humedad, luz, impactos y ubicación.

Su plataforma permite supervisar envíos por transporte terrestre, marítimo, aéreo y ferroviario y generar alertas cuando las condiciones se encuentran fuera de los rangos establecidos.

#### SWOT - Tive

**Fortalezas**

- Monitoreo en tiempo real de múltiples variables.
- Seguimiento multimodal de envíos.
- Amplia cobertura de conectividad.
- Diversos modelos de trackers según el nivel de monitoreo requerido.
- Alertas automáticas e historial de los envíos.
- Integraciones mediante API y webhooks.

**Debilidades**

- Orientación principal hacia monitoreo de mercancías en tránsito.
- La oferta puede resultar más compleja para organizaciones que solo necesitan monitorear instalaciones o lotes específicos.
- Los precios de los dispositivos principales dependen de cotización y volumen.

**Oportunidades**

- Crecimiento del comercio y logística de productos sensibles.
- Mayor demanda de monitoreo en tiempo real.
- Integración con sistemas empresariales y plataformas logísticas.

**Amenazas**

- Competidores globales con soluciones equivalentes de seguimiento IoT.
- Reducción del costo de sensores y conectividad que facilita la entrada de nuevas soluciones.
- Desarrollo de plataformas de monitoreo propias por grandes operadores logísticos.

### Roambee

Roambee desarrolla soluciones de visibilidad de cadena de suministro mediante dispositivos IoT y servicios cloud.

Sus soluciones permiten monitorear condiciones como temperatura y humedad, además de eventos relacionados con ubicación y transporte. La plataforma genera alertas y señales para apoyar la toma de decisiones durante operaciones logísticas.

#### SWOT - Roambee

**Fortalezas**

- Combina monitoreo de condiciones y ubicación.
- Dispositivos con múltiples sensores.
- Plataforma orientada a visibilidad logística empresarial.
- Integración mediante API.
- Opciones de servicio y suscripción según necesidades de monitoreo.
- Capacidad para trabajar con operaciones logísticas de gran escala.

**Debilidades**

- Solución de mayor alcance y complejidad que un sistema enfocado únicamente en conservación de alimentos.
- Costos dependientes de contratos, dispositivos y volumen de operaciones.
- Su propuesta está orientada a supply chain visibility de forma amplia y no exclusivamente al sector de alimentos perecibles.

**Oportunidades**

- Mayor adopción de IoT en transporte y logística.
- Demanda creciente de información en tiempo real.
- Necesidad empresarial de reducir interrupciones y pérdidas en cadenas de suministro.

**Amenazas**

- Alta competencia en plataformas de supply chain visibility.
- Evolución rápida de sensores IoT y plataformas de análisis.
- Aparición de alternativas especializadas de menor costo.

### SWOT - FreshSense

**Fortalezas**

- Enfoque específico en productos alimenticios perecibles.
- Integración de dispositivos IoT con una plataforma digital.
- Monitoreo de temperatura y humedad.
- Gestión centralizada de dispositivos y lotes.
- Generación de alertas ante condiciones que requieren atención.
- Arquitectura preparada para Web y Mobile.
- Propuesta orientada a trazabilidad y reducción de pérdidas.

**Debilidades**

- Producto aún en etapa de desarrollo y validación.
- Menor cantidad de variables monitoreadas frente a competidores internacionales.
- Menor cobertura tecnológica y comercial.
- Dependencia inicial de sensores y conectividad del dispositivo.
- Modelo comercial y precios aún pendientes de validación con usuarios empresariales.

**Oportunidades**

- Digitalización de empresas de distribución y comercialización de alimentos.
- Necesidad de reducir pérdidas provocadas por una conservación inadecuada.
- Crecimiento de soluciones IoT accesibles.
- Posibilidad de adaptar la solución a necesidades específicas del mercado local.
- Incorporación futura de sensores adicionales y analítica avanzada.

**Amenazas**

- Presencia de competidores internacionales consolidados.
- Reducción de precios de soluciones comerciales existentes.
- Resistencia de algunas empresas a reemplazar procesos manuales.
- Entrada de nuevos proveedores de soluciones IoT.
- Dependencia de la correcta instalación y conectividad de los dispositivos.

### Conclusión del análisis competitivo

El análisis evidencia que FreshSense participaría en un mercado en el que existen soluciones consolidadas con capacidades superiores en cobertura global, cantidad de sensores e infraestructura tecnológica.

Sensitech presenta una propuesta especialmente fuerte en monitoreo de cadena de frío tanto estacionario como en tránsito; Tive destaca por el seguimiento multimodal y la captura de múltiples variables en tiempo real; y Roambee ofrece una solución amplia de visibilidad y monitoreo de cadenas de suministro.

Frente a estos competidores, FreshSense no busca inicialmente competir por amplitud tecnológica, sino desarrollar una propuesta más específica para organizaciones que gestionan alimentos perecibles. Su diferenciación preliminar se basa en simplificar el monitoreo de temperatura y humedad y relacionarlo directamente con dispositivos, lotes, alertas y trazabilidad dentro de una experiencia centralizada.

Esta diferenciación deberá validarse posteriormente mediante entrevistas con los segmentos objetivo, principalmente para determinar qué variables necesitan monitorear, qué nivel de trazabilidad requieren y cuánto estarían dispuestos a invertir en una solución de este tipo.

### 2.1.2. Estrategias y tácticas frente a competidores

A partir del análisis competitivo, FreshSense plantea una estrategia de diferenciación enfocada en especialización, simplicidad y adaptación a las necesidades de empresas que gestionan alimentos perecibles.

Las principales estrategias y tácticas serán las siguientes:

- **Especialización en alimentos perecibles:** enfocar la experiencia, terminología, dashboards, lotes y alertas en procesos relacionados con almacenamiento y distribución de alimentos, evitando incorporar funcionalidades empresariales que no sean necesarias para los segmentos objetivo.

- **Implementación progresiva:** facilitar que las empresas puedan comenzar con un número reducido de dispositivos y ampliar posteriormente el monitoreo según sus necesidades.

- **Experiencia simplificada:** diferenciarse de plataformas empresariales de mayor complejidad mediante una interfaz centrada en las funciones principales: monitoreo, lotes, dispositivos, alertas y trazabilidad.

- **Adaptación al mercado objetivo:** utilizar las entrevistas B2B para identificar rangos de temperatura, procesos, reportes y necesidades específicas de empresas de distribución, productores y comercializadores.

- **Modelo comercial flexible:** evaluar alternativas de venta o provisión de dispositivos combinadas con una suscripción por acceso a la plataforma, evitando establecer precios definitivos antes de validar la disposición de pago de los segmentos.

- **Alertas orientadas a la acción:** priorizar notificaciones que permitan identificar rápidamente desviaciones y relacionarlas con un dispositivo o lote determinado.

- **Trazabilidad centralizada:** mantener el historial de lecturas y eventos de cada lote para facilitar la revisión de condiciones durante almacenamiento o distribución.

- **Evolución tecnológica gradual:** mantener una arquitectura que permita incorporar nuevos sensores, capacidades de conectividad y funciones analíticas a medida que el producto y las necesidades del mercado evolucionen.

Estas estrategias buscan que FreshSense compita inicialmente mediante una solución especializada y comprensible para empresas del sector alimentario, en lugar de intentar replicar desde el inicio la amplitud funcional de plataformas internacionales consolidadas.

## 2.2. Entrevistas

Las entrevistas constituyen una de las principales fuentes de información para comprender las necesidades, problemas y expectativas de los segmentos objetivo de FreshSense.

El proceso de investigación se enfoca en representantes de empresas que participan en actividades de almacenamiento, distribución, producción y comercialización de alimentos perecibles. A través de estas entrevistas se busca conocer cómo gestionan actualmente las condiciones de conservación de sus productos, qué dificultades enfrentan, qué herramientas utilizan y qué valor podría aportar una solución basada en dispositivos IoT y monitoreo digital.

Los resultados obtenidos permitirán validar los principales supuestos de FreshSense y servirán posteriormente como base para la elaboración de User Personas, User Task Matrix, User Journey Maps y demás artefactos de análisis.

Los segmentos considerados son:

- **Segmento 1: Empresas de distribución y cadena de frío.**
- **Segmento 2: Empresas productoras y comercializadoras de alimentos perecibles.**


### 2.2.1. Diseño de entrevistas

Las entrevistas serán de tipo semiestructurado, utilizando preguntas orientadas a conocer el contexto de trabajo del entrevistado, los procesos actuales de conservación de productos perecibles, los principales problemas encontrados, el uso de tecnología y la percepción de valor frente a una solución como FreshSense.

Las preguntas han sido diseñadas de acuerdo con las características de cada segmento objetivo y buscan obtener información suficiente para identificar necesidades, objetivos, frustraciones y patrones de comportamiento que posteriormente serán utilizados en la construcción de los arquetipos de usuario.

#### Segmento 1: Empresas de distribución y cadena de frío

1. ¿Cuál es su cargo dentro de la empresa y qué responsabilidades tiene relacionadas con el almacenamiento, transporte o distribución de productos perecibles?

2. ¿Qué tipo de productos perecibles maneja la empresa y en qué etapas del proceso considera más importante controlar sus condiciones de conservación?

3. ¿Cómo monitorean actualmente variables como temperatura y humedad durante el almacenamiento o transporte?

4. ¿Han tenido problemas relacionados con rupturas de la cadena de frío o condiciones fuera de los rangos permitidos? ¿Qué consecuencias generaron?

5. Cuando ocurre una incidencia, ¿cómo se enteran actualmente y cuánto tiempo suele tomar identificarla?

6. ¿Utilizan sensores, registradores, plataformas digitales u otras herramientas para realizar este monitoreo?

7. ¿Qué información considera más importante consultar durante una operación: temperatura, humedad, ubicación, estado del lote, historial de lecturas u otra?

8. ¿Qué tan útil sería recibir alertas automáticas cuando las condiciones se encuentren fuera de los límites establecidos?

9. ¿Cómo realizan actualmente el seguimiento de los lotes durante el almacenamiento y distribución?

10. En caso de una incidencia, ¿qué tan importante sería poder identificar rápidamente qué lote fue afectado y revisar su historial de condiciones?

11. ¿Qué características debería tener una solución de monitoreo para que resulte útil y fácil de implementar dentro de su empresa?

12. ¿Qué factores influirían más en la decisión de adoptar una solución como FreshSense: precio, precisión, facilidad de instalación, alertas, reportes, soporte u otros?

---

#### Segmento 2: Empresas productoras y comercializadoras de alimentos perecibles

1. ¿Cuál es su cargo dentro de la empresa y qué responsabilidades tiene relacionadas con producción, almacenamiento, calidad o comercialización?

2. ¿Qué tipo de alimentos perecibles maneja la empresa y cuáles requieren un mayor control de sus condiciones de conservación?

3. ¿Cómo verifican actualmente que los productos se encuentren almacenados bajo condiciones adecuadas?

4. ¿Qué problemas de conservación o deterioro se presentan con mayor frecuencia dentro de la empresa?

5. ¿Qué impacto generan estas pérdidas o deterioros en términos económicos, operativos o de calidad?

6. ¿Utilizan sensores, termómetros, hojas de cálculo, sistemas de inventario u otras herramientas para controlar las condiciones de almacenamiento?

7. ¿Con qué frecuencia revisan actualmente variables como temperatura y humedad?

8. ¿Qué tan útil sería contar con información de estas condiciones en tiempo real y recibir alertas cuando exista una desviación?

9. ¿Cómo identifican y realizan actualmente el seguimiento de los diferentes lotes de productos?

10. Si se detecta un problema de conservación, ¿qué tan sencillo es identificar cuáles lotes podrían haber sido afectados?

11. ¿Qué características considera indispensables en una plataforma de monitoreo de productos perecibles?

12. ¿Qué factores serían más importantes al momento de adoptar una solución como FreshSense: costo, facilidad de uso, precisión, trazabilidad, alertas, reportes u otros?

### 2.2.2. Registro de entrevistas

#### Segmento 1: Empresas de distribución y cadena de frío


##### Entrevista 1

| Dato | Información |
| --- | --- |
| Nombre y apellidos | Carlos Mendoza Ruiz |
| Edad | 26 años |
| Distrito | Callao |
| Empresa / sector | Distribución refrigerada de alimentos |
| Cargo | Supervisor de Logística |
| Inicio de entrevista | 00:00 |
| Duración | 08:42 |
| Enlace | [Ver entrevista](URL) |

![Evidencia entrevista](Assets/EntrevistaS21.png)

**Resumen:**  
Carlos Mendoza trabaja como supervisor de logística en una empresa dedicada a la distribución refrigerada de alimentos. Dentro de sus funciones supervisa el almacenamiento y transporte de productos como lácteos, carnes y alimentos congelados.

Explicó que actualmente realizan el control de temperatura mediante termómetros instalados en cámaras de refrigeración y registradores ubicados en algunas unidades de transporte. Parte de la información es revisada manualmente y posteriormente registrada en hojas de cálculo.

Señaló que uno de los principales problemas ocurre cuando existen variaciones de temperatura durante el transporte y estas se detectan recién al finalizar el recorrido. Este tipo de incidencias puede ocasionar revisión adicional de mercadería, retrasos y, en algunos casos, pérdida de productos.

Considera que recibir alertas automáticas sería especialmente útil para reaccionar antes de que una desviación genere un daño importante. Entre la información que considera prioritaria se encuentran la temperatura, humedad, ubicación del producto, identificación del lote y el historial de lecturas.

También indicó que una solución como FreshSense debería ser fácil de instalar, contar con información clara y permitir revisar rápidamente qué producto o lote fue afectado. Para una eventual adopción considera importantes la precisión de los sensores, el precio y la disponibilidad de soporte técnico.


##### Entrevista 2

| Dato | Información |
| --- | --- |
| Nombre y apellidos | Carlos Guimaraes |
| Edad | 27 años |
| Distrito | Villa El Salvador |
| Empresa / sector | Producción y almacenamiento de carnes y productos congelados |
| Cargo | Jefe de Almacén |
| Inicio de entrevista | 0:00 |
| Duración | 08:36 |
| Enlace | [Ver entrevista](https://drive.google.com/file/d/1Q8i84GD9mqFdKOLVYLR2PqdWQVT1MYik/view?usp=drive_link) |

![Evidencia entrevista](Assets/1.png)

**Resumen:**  
Carlos Guimaraes se desempeña como jefe de almacén en una empresa que trabaja con carnes y productos congelados. Dentro de sus funciones se encuentra supervisar el ingreso y salida de mercadería, verificar las condiciones de las cámaras frigoríficas y coordinar el movimiento de los diferentes lotes almacenados.

Explicó que los controles se realizan mediante termómetros instalados en las cámaras y verificaciones periódicas del personal. La identificación de lotes se gestiona mediante registros internos y etiquetas asociadas a cada ingreso de mercadería.

Indicó que los principales problemas pueden aparecer cuando existen fallas en los equipos de refrigeración o cuando las cámaras permanecen abiertas durante demasiado tiempo. Estas situaciones pueden ocasionar incrementos temporales de temperatura que deben ser identificados rápidamente.

Considera especialmente útil contar con alertas que indiquen cuándo una cámara o producto se encuentra fuera del rango permitido. También mencionó que sería importante identificar rápidamente qué lotes se encontraban almacenados durante una incidencia.

Para una posible implementación, considera relevantes el costo del sistema, la facilidad de instalación, la confiabilidad de las mediciones y la disponibilidad de soporte técnico.


##### Entrevista 3

| Dato | Información |
| --- | --- |
| Nombre y apellidos | Javier Torres Castillo |
| Edad | 26 años |
| Distrito | San Luis |
| Empresa / sector | Distribución mayorista de alimentos perecibles |
| Cargo | Responsable de Cadena de Frío |
| Inicio de entrevista | 00:00 |
| Duración | 08:57 |
| Enlace | [Ver entrevista](https://drive.google.com/file/d/1_Jg-67dLuuAXt6bTV69x12lShay-IJ0v/view?usp=drive_link) |

![Evidencia entrevista](Assets/3.png)

**Resumen:**  
Javier Torres trabaja como responsable de cadena de frío en una empresa distribuidora de productos perecibles. Sus principales responsabilidades incluyen supervisar las condiciones de almacenamiento, coordinar despachos y verificar que los productos mantengan condiciones adecuadas durante su traslado.

Actualmente utilizan termómetros digitales y controles manuales realizados por el personal. Algunos vehículos disponen de dispositivos capaces de registrar temperatura, aunque señaló que no toda la información se encuentra disponible en una única plataforma.

Según su experiencia, las principales incidencias están relacionadas con variaciones de temperatura ocasionadas por aperturas prolongadas, problemas de refrigeración o retrasos durante la distribución. Estas situaciones pueden afectar la calidad de los productos y ocasionar devoluciones.

Considera que contar con alertas automáticas y un historial asociado a cada lote ayudaría a detectar problemas más rápidamente y facilitaría la identificación de responsabilidades frente a una incidencia.

Entre las características que considera indispensables mencionó facilidad de uso, precisión de las mediciones, disponibilidad de información histórica y generación de reportes. También considera importante que la solución pueda implementarse progresivamente, comenzando con determinados almacenes o vehículos antes de extenderse al resto de la operación.


#### Segmento 2: Empresas productoras y comercializadoras de alimentos perecibles

##### Entrevista 1

| Dato | Información |
| --- | --- |
| Nombre y apellidos | María Fernanda Rojas Díaz |
| Edad | 36 años |
| Distrito | Santa Anita |
| Empresa / sector | Producción y comercialización de productos lácteos |
| Cargo | Supervisora de Calidad |
| Inicio de entrevista | 00:00 |
| Duración | 09:18 |
| Enlace | [Ver entrevista](https://drive.google.com/file/d/1yaP9FCvV9rKo09GO2Eu2jYF9UUS8Ujob/view?usp=drive_link) |

![Evidencia entrevista](Assets/2.png)

**Resumen:**  
María Fernanda Rojas trabaja como supervisora de calidad en una empresa dedicada a la producción y comercialización de productos lácteos. Entre sus responsabilidades se encuentra verificar las condiciones de almacenamiento de productos terminados y coordinar controles relacionados con temperatura y calidad.

Comentó que actualmente utilizan termómetros digitales y realizan registros periódicos de temperatura en las áreas de almacenamiento. Parte de esta información es trasladada posteriormente a hojas de cálculo para mantener evidencia de los controles realizados.

Según indicó, uno de los principales problemas se presenta cuando una desviación ocurre entre dos controles manuales, debido a que puede pasar cierto tiempo antes de ser detectada. Esto puede generar revisiones adicionales del producto y, en algunos casos, la separación de lotes hasta confirmar que mantienen condiciones adecuadas.

Considera que contar con información disponible en tiempo real y recibir alertas automáticas facilitaría el trabajo del área de calidad. También considera importante poder revisar el historial de temperatura y humedad correspondiente a cada lote.

Entre los factores más relevantes para adoptar una solución de este tipo destacó la precisión de los sensores, la facilidad de uso, la generación de reportes y la posibilidad de acceder a información histórica.


##### Entrevista 2

| Dato | Información |
| --- | --- |
| Nombre y apellidos | Andrea Salazar Paredes |
| Edad | 29 años |
| Distrito | Ate |
| Empresa / sector | Operador logístico de productos refrigerados |
| Cargo | Coordinadora de Operaciones |
| Inicio de entrevista | 00:00 |
| Duración | 09:15 |
| Enlace | [Ver entrevista](https://drive.google.com/file/d/1iQW9Vu0lRPL9HhDX3PIfNHNQqrBESufE/view?usp=drive_link) |

![Evidencia entrevista](Assets/5.png)

**Resumen:**  
Andrea Salazar se desempeña como coordinadora de operaciones en una empresa que almacena y distribuye productos refrigerados para diferentes clientes del sector alimentario.

Indicó que la empresa trabaja con cámaras de refrigeración y vehículos acondicionados para mantener determinadas temperaturas. El control se realiza mediante sensores en algunos puntos de almacenamiento y verificaciones periódicas efectuadas por el personal.

Comentó que una dificultad importante es que la información de almacenamiento, transporte y lotes se encuentra distribuida entre diferentes registros. Cuando ocurre una incidencia, identificar cuándo sucedió y qué mercadería estuvo expuesta puede requerir revisar distintas fuentes de información.

Para ella, una plataforma centralizada que permita relacionar dispositivos, lotes e incidencias facilitaría considerablemente el trabajo operativo. Considera especialmente importantes las alertas en tiempo real y la posibilidad de consultar un historial de temperatura y humedad.

Señaló también que una solución tecnológica debería ser sencilla de utilizar por diferentes perfiles de empleados y ofrecer reportes que puedan ser revisados posteriormente. En una decisión de compra priorizaría la confiabilidad, facilidad de implementación y capacidad de generar alertas oportunas.


##### Entrevista 3

| Dato | Información |
| --- | --- |
| Nombre y apellidos | Daniela Vargas Medina |
| Edad | 22 años |
| Distrito | Lurín |
| Empresa / sector | Comercialización y almacenamiento de frutas y vegetales |
| Cargo | Coordinadora de Operaciones |
| Inicio de entrevista | 00:00 |
| Duración | 09:04 |
| Enlace | [Ver entrevista](https://drive.google.com/file/d/1AqFpCV5FGpSXy3RIi9gN7BdsXJm4ywSU/view?usp=drive_link) |

![Evidencia entrevista](Assets/4.png)

**Resumen:**  
Daniela Vargas trabaja como coordinadora de operaciones en una empresa dedicada al almacenamiento y comercialización de frutas y vegetales. Sus responsabilidades incluyen coordinar el ingreso de productos, revisar el inventario disponible y supervisar las condiciones generales de almacenamiento.

Comentó que algunos controles de temperatura se realizan mediante equipos instalados en las cámaras, mientras que la revisión de humedad y estado de los productos depende en mayor medida de inspecciones realizadas por el personal.

Uno de los problemas que identifica es que diferentes productos requieren condiciones distintas de conservación y no siempre resulta sencillo mantener un seguimiento constante de todos los lotes almacenados.

Considera que una plataforma que permita visualizar lotes, condiciones ambientales e incidencias desde un mismo lugar ayudaría a mejorar el control de la operación. También considera útil contar con alertas configurables según el tipo de producto.

Entre las funcionalidades que considera importantes destacó el historial de mediciones, los reportes, la identificación de lotes afectados y una interfaz sencilla que pueda ser utilizada tanto por responsables de operaciones como por personal de calidad.


### 2.2.3. Análisis de entrevistas

#### Segmento 1: Empresas de distribución y cadena de frío

A partir de las tres entrevistas realizadas, se identificó que el **100 % de los entrevistados realiza algún control de temperatura**, aunque todos mencionaron que parte del proceso todavía depende de verificaciones manuales.

El **66.7 %** indicó que utiliza sensores o registradores digitales en determinadas etapas, pero la información no siempre se encuentra centralizada. Asimismo, el **100 % considera útil recibir alertas automáticas** cuando las condiciones salen de los rangos establecidos.

También se observó que el **100 % considera importante relacionar las condiciones registradas con los lotes monitoreados**, principalmente para identificar rápidamente posibles incidencias.

En este segmento, las principales necesidades identificadas son el monitoreo continuo, las alertas oportunas, la trazabilidad y la centralización de la información.

#### Segmento 2: Empresas productoras y comercializadoras de alimentos perecibles

En este segmento, el **100 % de los entrevistados utiliza algún mecanismo para controlar la temperatura**, aunque las tres empresas también realizan verificaciones manuales periódicas.

El **100 % considera útil contar con información en tiempo real y alertas automáticas**, especialmente para detectar desviaciones antes de que afecten la calidad de los productos.

Además, el **100 % considera relevante asociar las condiciones de almacenamiento con los lotes**, mientras que el **66.7 %** destacó la utilidad de contar con reportes e historiales de mediciones.

Las principales necesidades identificadas son el monitoreo en tiempo real, la gestión de lotes, las alertas y el acceso a información histórica.

#### Conclusión general

En ambos segmentos se observa una necesidad común de mejorar el control de las condiciones de conservación mediante una solución más centralizada y automatizada.

Los resultados respaldan principalmente cuatro funcionalidades de FreshSense: **monitoreo de temperatura y humedad, alertas automáticas, gestión de lotes e historial de mediciones**.

2.3. Needfinding.

2.3.1. User Personas.

2.3.2. User Task Matrix.

2.3.3. User Journey Mapping.

2.3.4. Empathy Mapping.

2.4. Big Picture EventStorming.

2.5. Ubiquitous Language.

Capítulo III: Requirements Specification

3.1. User Stories.

3.2. Impact Mapping.

3.3. Product Backlog.

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
