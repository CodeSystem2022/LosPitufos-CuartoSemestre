console.log('inicio de programa');
setTimeout(() => {
    console.log('primer timeout')
}, 3000);

setTimeout(() => {
    console.log('segunto timeout')
}, 0);

setTimeout(() => {
    console.log('tercer timeout')
}, 0);
console.log('fin del programa');