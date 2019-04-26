< script >

    var names = localStorage.Book_Name;
names = names + "!";
var quantity = localStorage.Quantity;
quantity = quantity + "!";
var price = localStorage.Price;
price = price + "!";
var t = "";
var q = "";
var p = "";
var n = "";
var an = [];
var ap = [];
var aq = [];
if (names) {
    for (var i = 0; i < names.length; i++) {

        if (i >= 5) {
            n = n + names[i];

        }

    }

    console.log(n);
    for (var i = 0; i < n.length; i++) {
        var t = t + n[i];
        if (n[i] == "!") {
            t = t.replace("!", "");
            an.push(t);
            t = "";

        }

    }
    console.log(an);
    for (var i = 0; i < quantity.length; i++) {

        if (i >= 5) {
            q = q + quantity[i];

        }

    }


    for (var i = 0; i < q.length; i++) {
        var t = t + q[i];
        if (q[i] == "!") {
            t = t.replace("!", "");
            aq.push(t);
            t = "";

        }

    }

    for (var i = 0; i < price.length; i++) {

        if (i >= 5) {
            p = p + price[i];

        }

    }


    for (var i = 0; i < p.length; i++) {
        var t = t + p[i];
        if (p[i] == "!") {
            t = t.replace("!", "");
            ap.push(t);
            t = "";

        }

    }
}
var at = [];
var min = "1";
var max = "100";

var myTable = "<table id='datatable'><tr><th >Book Name</th>";

myTable += "<th >Unit Price</th>";
myTable += "<th>Quanity</th>";

myTable += "<th>Total Price</th></tr>";




for (var i = 0; i < an.length; i++) {
    var tp = parseInt(aq[i]) * parseInt(ap[i]);

    var sp = tp + "";

    at.push(sp);



    myTable += "<td>" + an[i] + "</td>";

    myTable += "<td>" + ap[i] + "</td>";

    myTable += "<td>" + aq[i] + "</td>";
    myTable += "<td>" + sp + "</td></tr>";


}
var totalprice = 0;
for (var i = 0; i < ap.length; i++) {
    totalprice = totalprice + (parseInt(ap[i]) * parseInt(aq[i]));

}



localStorage.setItem("TotalPrice", totalprice);
myTable += "<tr><td colspan='6'>total price:" + totalprice + "</td></tr>"
myTable += "</table>";
document.write(myTable);


<
/script>