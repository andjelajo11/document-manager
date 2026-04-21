🎬  Multimedia Documents App
🧾 Overview

Handler of Multimedia Documents is a GUI-based, component-oriented software tool designed for creating, managing, and organizing complex multimedia documents.

The system supports text, images, vector graphics, audio, video, and animations, enabling users to work with dynamically structured documents and collections.

---

## 🏗️ Architecture & Design

App is built as a **modular, extensible framework** based on a **component-oriented architecture**, where the system is composed of dynamically integrated components via a **plug-in mechanism**.

### Key Architectural Concepts

* 🧩 **Component-Based Architecture**
* 🔌 **Plug-and-Play Integration (Plugin System)**
* 🧠 **MVC (Model-View-Controller) Pattern**
* ⚙️ **Event-Driven GUI Application**

### Design Patterns Used

* **Bridge**
* **Composite**
* **Singleton**
* **State**
* **Observer**
* **Factory Method / Abstract Factory**
* **Command**

These patterns ensure scalability, maintainability, and flexibility of the system.

---

## 🧠 Core Functionalities

### 📄 Document Management

* Creation and manipulation of complex documents
* Support for hierarchical structure:

  * Document → Pages → Slots → Elements

### 🧱 Supported Elements

* ✏️ Text (rich formatting, paragraphs, chapters)
* 🖼️ Raster images
* 🎨 Vector graphics
* 🔊 Audio
* 🎥 Video
* 🎞️ Animations (composite elements)

### 📚 Collections & Workspaces

* Organize documents into **collections**
* Collections can contain:

  * Documents
  * Other collections (nested structure)
* Manage multiple **workspaces**

### 🔗 Content Sharing

* Share:

  * Entire documents
  * Pages between documents
  * Slots and elements across pages

### 👥 User Management

* User administration component
* Role-based interaction with the system

---

## 🖥️ GUI Structure

The application provides a structured graphical interface consisting of:

* Title Bar
* Menu Bar
* Toolbar
* Workspace Area
* Operational Area
* Status Bar

---

## ⚙️ Technology Stack

* **Language:** Python
* **GUI Framework:** PySide (Qt)
* **Database:** MySQL (`mysql.connector`)
* **Modeling Tool:** Astah Professional (UML diagrams)

---

## 🔄 Development Methodology

The project follows:

### 🚀 Agile Development

* Team-based development (3–5 members)
* Iterative progress
* Continuous integration

### 🧪 Evolutionary Prototyping

* Incremental development of components
* Integration through a central component

### 📐 Model-Driven Engineering

* UML-based system design:

  * Use Case Diagrams
  * Class Diagrams
  * Sequence Diagrams
  * State Diagrams
  * Activity Diagrams

---

## 🧩 System Components

Mandatory components include:

* **Integrative Component**

  * Manages configuration and orchestration of components

* **Plugin Manager**

  * Enables dynamic loading and integration

* **User Administration Component**

* **Document Storage Component**

  * Handles file system and metadata

* **Help Component**

  * Provides user guidance

* **Domain Components**

  * Handle document structure and multimedia elements

---

## ▶️ Getting Started

### Prerequisites

* Python 3.x
* PySide
* MySQL Server

### Installation

```bash
git clone https://github.com/your-username/rummdok.git
cd rummdok
pip install -r requirements.txt
```

### Run the Application

```bash
python main.py
```

---

## 📁 Project Structure (Conceptual)

```bash
rummdok/
│
├── core/              # Core system & integrative component
├── components/        # Individual components (plugins)
├── gui/               # UI (PySide)
├── models/            # Document structure (MVC - Model)
├── controllers/       # Application logic
├── views/             # GUI rendering
├── database/          # MySQL integration
└── docs/              # UML & documentation
```

---

## 🎯 Project Vision

RuMmDok is designed as a **general-purpose framework** for organizations and individuals working with **complex, multimedia-rich documents**.

Its goal is to provide:

* Flexible document structuring
* Extensible architecture
* Scalable component integration

---

## 👩‍💻 Authors

This project was developed by a team of five as part of the Software Development Methodology course , following a model-driven and component-based architecture approach, with a strong emphasis on collaboration, modular design, and software engineering best practices.

---

## 📌 Notes

* This project emphasizes **architecture and design principles** over production-level deployment.
* Future improvements may include:

  * Cloud storage integration
  * Real-time collaboration
  * Advanced multimedia editing tools
