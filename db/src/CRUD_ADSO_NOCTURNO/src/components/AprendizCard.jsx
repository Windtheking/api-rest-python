// Inyectar estilos una sola vez
if (!document.getElementById("aprendiz-card-styles")) {
  const tag = document.createElement("style");
  tag.id = "aprendiz-card-styles";
  tag.textContent = styles;
  document.head.appendChild(tag);
}

/**
 * AprendizCard – tarjeta individual de un aprendiz.
 * Props:
 *   aprendiz: { id, nombre, correo, edad }
 *   onClick: (id: number) => void
 *   index: number  (para el delay de animación)
 */
export default function AprendizCard({ aprendiz, onClick, index = 0 }) {
  return (
    <div
      className="card"
      style={{ animationDelay: `${index * 0.08}s` }}
      onClick={() => onClick(aprendiz.id)}
    >
      <p className="card-id">#{String(aprendiz.id).padStart(3, "0")}</p>
      <p className="card-name">{aprendiz.nombre}</p>
      <div className="card-info">
        <div className="info-row">
          <span className="icon">✉</span>
          <span className="value">{aprendiz.correo}</span>
        </div>
        <div className="info-row">
          <span className="icon">◈</span>
          <span className="value">{aprendiz.edad} años</span>
        </div>
      </div>
    </div>
  );
}