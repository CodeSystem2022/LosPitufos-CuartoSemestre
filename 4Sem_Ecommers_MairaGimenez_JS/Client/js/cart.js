const modalContainer = document.getElementById("modal-container");
const modalOverlay = document.getElementById("modal-overlay");

const cartBtn = document.getElementById("cart-btn")
const cartCounter = document.getElementById("cart-counter")

const displayCart = () =>   {
    //modal header
    const modalHeader = document.createElement("div");

    const modalClose = document.createElement("div");
    modalClose.innerText = "❌"
    modalClose.className = "modal-close";
    modalHeader.append(modalClose);

    modalClose.addEventListener("Click", ()=>   {
        modalContainer.style.display = "none";
        modalOverlay.style.display = "none";
    })

    const modalTitle = document.createElement("div");
    modalTitle.innerText = "cart";
    modalTitle.className = "modal-title";
    modalHeader.append(modalTitle);

    modalContainer.append(modalHeader);

    //miodal body
    if(cart.lenght>0) {
    cart.forEach((product)=>    {
        const modalBody = document.createElement("div");
        modalBody.className = "modal-body"
        modalBody.innerHTML = ´
        <div class="product">
            <img class="product img" scr="$ {product.img}"/>
            <div class="product-info">
                <h4>${product.productName}</h4>
            </div>
          <div class="quantity">
            <span class="quantity-btn-decrese">-</span>
            <span class="quantity-btn-input">$  {product.quanty }</span>
            <span class="quantity-btn-decrese">+</span>
          </div>
          <div>
            <div class="price">$    {product.price * product.quanty }</div>
            <div class="delete-product">❌</div>
          </div>
        </div>
         ´;
         modalContainer.append(modalBody);
    });
    }
    else{
    const modalText = dcocument.createElement("h2");
    modalContainer.closest.className="modal-body";
    modalText.innerText="your cart is empty";
    modalContainer.append(modalText);
   }
};

cartBtn.addEventListener("Click", displayCart);

const displayCartCounter =()=>  {
  const cartLenght = cart.reduce((acc,el)=>acc+el.quanty,0);
  if(cartLenght>0)  {
    cartCounter.style.display="block";
    cartCounter.innerText=cartLenght;
  }
  else{
    cartCounter.style.display="none";
  }
  
}