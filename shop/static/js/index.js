
function add_to_cart(product_id) {
    var product_data = $("#"+product_id);

    $.ajax({
        type : "POST",
        url : "add_to_cart",
        data: {
            id: product_data.find("input[name=product_id]").val(),
            qty: product_data.find("input[name=qty]").val(),
        }
    });
}

function edit_amount(element_id, product_id) {
    
    $("dd#"+product_id).find("span").text($("#"+element_id).val());

    $.ajax({
        type : "POST",
        url : "shopping_cart",
        data: {
            id: product_id,
            qty: $("#"+element_id).val(),
        }
    });

}