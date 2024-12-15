"use client";

import { useState } from "react";
import data from "./data.json";

export default function Home() {
  const [posts, setPosts] = useState(data); // Estado inicial con los datos del JSON
  const [showModal, setShowModal] = useState(false); // Controla si el modal está abierto
  const [modalType, setModalType] = useState(""); // Indica si es "request" o "service"
  const [formData, setFormData] = useState({
    title: "",
    description: "",
    user: "",
    price: "",
  });

  // Manejar cambios en los campos del formulario
  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  // Agregar una nueva publicación
  const handleAddPost = () => {
    if (!formData.title || !formData.description || !formData.user || !formData.price) {
      alert("Por favor completa todos los campos");
      return;
    }

    const newPost = {
      id: posts.length + 1, // Genera un ID único
      type: modalType,
      ...formData,
      price: parseInt(formData.price, 10), // Convertir el precio a número
    };

    setPosts([...posts, newPost]); // Agregar al estado
    setFormData({ title: "", description: "", user: "", price: "" }); // Limpiar el formulario
    setShowModal(false); // Cerrar el modal
  };

  // Filtrar publicaciones según el filtro seleccionado
  const [filter, setFilter] = useState("all");
  const filteredPosts = posts.filter((post) => {
    if (filter === "all") return true;
    return post.type === filter;
  });

  return (
    <div style={pageStyle}>
      <div style={contentStyle}>
        <header style={headerStyle}>
          <h1 style={titleStyle}>Jobbly</h1>
          <p style={subtitleStyle}>
            Plataforma exclusiva para estudiantes de la Universidad Austral.
            Conecta con compañeros para solicitar o ofrecer servicios.
          </p>
        </header>

        {/* Filtros */}
        <div style={filterStyle}>
          <button style={buttonStyle} onClick={() => setFilter("all")}>Ver todo</button>
          <button style={buttonStyle} onClick={() => setFilter("request")}>Ver Solicitudes</button>
          <button style={buttonStyle} onClick={() => setFilter("service")}>Ver Servicios</button>
        </div>

        {/* Botones principales */}
        <div style={actionButtonsStyle}>
          <button
            style={actionButtonStyle}
            onClick={() => {
              setModalType("request");
              setShowModal(true);
            }}
          >
            Solicitar un servicio
          </button>
          <button
            style={actionButtonStyle}
            onClick={() => {
              setModalType("service");
              setShowModal(true);
            }}
          >
            Ofrecer un servicio
          </button>
        </div>

        {/* Publicaciones */}
        <div style={postsStyle}>
          {filteredPosts.length > 0 ? (
            filteredPosts.map((post) => (
              <div key={post.id} style={postCardStyle}>
                <h2 style={postTitleStyle}>{post.title}</h2>
                <p>{post.description}</p>
                <p>
                  <strong>Precio:</strong> ${post.price.toLocaleString()} CLP
                </p>
                <p>
                  <strong>Contacto:</strong> {post.user}@alumnos.uach.cl
                </p>
                <span style={postTypeStyle}>
                  {post.type === "request" ? "Solicitud" : "Servicio"}
                </span>
              </div>
            ))
          ) : (
            <p>No hay publicaciones disponibles.</p>
          )}
        </div>
      </div>

      {/* Modal */}
      {showModal && (
        <div style={modalOverlayStyle}>
          <div style={modalStyle}>
            <h2>{modalType === "request" ? "Solicitar un servicio" : "Ofrecer un servicio"}</h2>
            <label>
              Título:
              <input
                type="text"
                name="title"
                value={formData.title}
                onChange={handleInputChange}
                style={inputStyle}
              />
            </label>
            <label>
              Descripción:
              <textarea
                name="description"
                value={formData.description}
                onChange={handleInputChange}
                style={textareaStyle}
              />
            </label>
            <label>
              Usuario (sin @alumnos.uach.cl):
              <input
                type="text"
                name="user"
                value={formData.user}
                onChange={handleInputChange}
                style={inputStyle}
              />
            </label>
            <label>
              Precio (CLP):
              <input
                type="number"
                name="price"
                value={formData.price}
                onChange={handleInputChange}
                style={inputStyle}
              />
            </label>
            <div style={modalButtonsStyle}>
              <button onClick={() => setShowModal(false)} style={buttonStyle}>
                Cancelar
              </button>
              <button onClick={handleAddPost} style={saveButtonStyle}>
                Guardar
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

// Estilos
const pageStyle = {
  backgroundColor: "#f9f9f9",
  minHeight: "100vh",
  padding: "20px",
  fontFamily: "'Poppins', sans-serif",
};

const contentStyle = {
  maxWidth: "900px",
  margin: "0 auto",
};

const headerStyle: React.CSSProperties = {
  textAlign: "center", // Asegúrate de que sea un valor válido
  marginBottom: "20px",
};


const titleStyle = {
  fontSize: "3rem",
  fontFamily: "'Raleway', sans-serif",
  color: "#2c3e50",
  fontWeight: 700,
  margin: "0 0 10px 0",
  letterSpacing: "2px",
};

const subtitleStyle = {
  fontSize: "1.2rem",
  fontFamily: "'Open Sans', sans-serif",
  color: "#7f8c8d",
  lineHeight: "1.5",
};

const filterStyle = {
  display: "flex",
  justifyContent: "center",
  gap: "15px",
  marginBottom: "20px",
};

const actionButtonsStyle = {
  display: "flex",
  justifyContent: "space-between",
  marginBottom: "20px",
};

const buttonStyle = {
  padding: "10px 20px",
  fontSize: "16px",
  cursor: "pointer",
  border: "1px solid #ddd",
  backgroundColor: "#f9f9f9",
  borderRadius: "5px",
};

const actionButtonStyle = {
  ...buttonStyle,
  backgroundColor: "#0070f3",
  color: "#fff",
};

const postsStyle: React.CSSProperties = {
  display: "flex",
  flexDirection: "column", // Asegúrate de que sea un valor válido
  gap: "10px",
};


const postCardStyle = {
  border: "1px solid #ddd",
  padding: "20px",
  borderRadius: "10px",
  backgroundColor: "#fff",
  boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
};

const postTitleStyle = {
  fontSize: "1.6rem",
  fontWeight: 600,
  color: "#2c3e50",
  marginBottom: "10px",
};

const postTypeStyle = {
  fontStyle: "italic",
  color: "gray",
};

const modalOverlayStyle: React.CSSProperties = {
  position: "fixed",
  top: 0,
  left: 0,
  width: "100%",
  height: "100%",
  backgroundColor: "rgba(0, 0, 0, 0.5)",
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
};
const modalStyle = {
  backgroundColor: "#fff",
  padding: "30px",
  borderRadius: "10px",
  width: "400px",
  boxShadow: "0 4px 8px rgba(0, 0, 0, 0.2)",
};

const inputStyle = {
  display: "block",
  width: "100%",
  marginTop: "5px",
  marginBottom: "15px",
  padding: "12px",
  border: "1px solid #ddd",
  borderRadius: "5px",
};

const textareaStyle = {
  ...inputStyle,
  height: "100px",
};

const modalButtonsStyle = {
  display: "flex",
  justifyContent: "flex-end",
  gap: "10px",
};

const saveButtonStyle = {
  ...buttonStyle,
  backgroundColor: "#0070f3",
  color: "#fff",
};
