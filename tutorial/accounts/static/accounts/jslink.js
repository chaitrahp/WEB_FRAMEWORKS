var button=document.querySelectorAll(".buton");
for(i=0;i<button.length;i++)
{
			button[i].addEventListener("click",handler,false);
			
}

			function handler(e)
			{
				alert("Added to the cart");
				var parent3=e.currentTarget.parentElement.parentElement.parentElement;
				var parent2=e.currentTarget.parentElement.parentElement;
				var p=parent3.querySelector("h3").textContent;
				var booknames = parent3.querySelector("h1").textContent;
				var pr = p.replace('Price:Rs ','');
			
				var n=localStorage.getItem("Book_Name")+"!"+booknames;
				localStorage.setItem("Book_Name", n);
				var quantity= parent2.querySelector(".quant").value;
				
				if(quantity<1 ||quantity>100)
				{
					quantity=1;
					
				}
				var t=localStorage.getItem("Quantity")+"!"+quantity;
				localStorage.setItem("Quantity", t);
				var pp=localStorage.getItem("Price")+"!"+pr;
				localStorage.setItem("Price",pp);
			
			}