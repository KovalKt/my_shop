
function add_to_cart(product_id) {
    var product_data = $("#"+product_id);
    console.log(product_data.find("input[name=product_id]"));
    $.ajax({
        type : "POST",
        url : "add_to_cart",
        data: {
            id: product_data.find("input[name=product_id]").val(),
            qty: product_data.find("input[name=qty]").val(),
        }
    });
}

// function edit_amount(button, products_available) {

//   // var $button = $(this);
//   var oldValue = button.parent().find("input").val();

//   if (button.text() == "+") {
//       var newVal = parseFloat(oldValue) + 1;
//     } else {
//    // Don't allow decrementing below zero
//     if (oldValue > 0) {
//       var newVal = parseFloat(oldValue) - 1;
//     } else {
//       newVal = 0;
//     }
//   }

//   button.parent().find("input").val(newVal);

// }