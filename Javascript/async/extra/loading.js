function load(type, name, time) {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log(`[${type}] Cargado: ${name} (${time}ms)`);
      resolve(`${type}: ${name}`);
    }, time);
  });
}

async function loadWebsite() {
  console.log("Iniciando la carga del sitio web...\n");

  console.log("--- Cargando Estilos ---");
  await load("Estilo", "styles.css", 500);

  console.log("\n--- Cargando Imágenes en paralelo ---");
  const imgPromises = [
    load("Imagen", "logo.png", 1200),
    load("Imagen", "banner.jpg", 1500),
    load("Imagen", "avatar.png", 800),
  ];
  await Promise.all(imgPromises);
  console.log("Todas las imágenes han sido cargadas.");

  console.log("\n--- Cargando Scripts en secuencia ---");
  const scripts = [
    { name: "analytics.js", time: 1000 },
    { name: "main.js", time: 1200 },
    { name: "app.js", time: 800 },
  ];

  for (const script of scripts) {
    await load("Script", script.nombre, script.tiempo);
  }
  console.log("Todos los scripts han sido cargados.");

  console.log("\n¡Todo el sitio web ha sido cargado con éxito!");
}

loadWebsite();
