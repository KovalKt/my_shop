
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
    $.ajax({
        type : "POST",
        url : "shopping_cart",
        data: {
            id: product_id,
            qty: $("#"+element_id).val(),
        }
    });
}

function remove_item(container_id, product_id) {
    $("#"+container_id).hide();
    $.ajax({
        type : "POST",
        url : "remove_item",
        data: {
            id: product_id
        }
    });
}
