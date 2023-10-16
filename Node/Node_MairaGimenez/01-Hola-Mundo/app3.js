console.log("Inicio de programa");
setTimeout(() =>    {
    console.log("Primer TIMEOUT");
}, 3000);

setTimeout(() =>    {
    console.log("Segundo TIMEOUT");
}, 0);

setTimeout(() =>    {
    console.log("Tercero TIMEOUT");
}, 0);

console.log("Fin de programa");