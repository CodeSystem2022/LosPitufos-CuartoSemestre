function soyAsincrona(){
    setTimeout(function (micallback)  {
        console.log('hola , soy una funcion asincronica');
        micallback();
        
    }, 1000);
    
    
}
console.log('iniciamos el proceso...');
soyAsincrona(function () {

console.log("terminando el proceso...");

});



