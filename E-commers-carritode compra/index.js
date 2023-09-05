const shopContent = document.getElementById("shopContent");
const cart  = []; // este es nuestro aray para el carrito de compra

producto.forEach((product)) =>{
 const content = document.createElement("div");
 content.innerHTML = ´
 <img src="${product.img}">
 <h3>${product.productName}</h3>
 <p>${product.price} $</p>

      ´;
    shopContent.append(content);

    const buButton = document.createElement("button");
    buyButton.innerTEXT = "COMPRAR";

    content.append(buButton);

    buyButton.addEventListener("click", ()=>{
        cart.push({
            id: product.id,
            productName: product.productName,
            price: product.price,
            quanty: product.quanty,
            img: product.img,
        })
         console.log(cart)
    })



});
