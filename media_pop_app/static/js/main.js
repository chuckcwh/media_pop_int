$(document).ready(function() {

//    show keyCombos from database
    function keycombo_data(){
        $.ajax ({
            url: "/getKeys/",
            type: "GET",
            dataType: "json",
            success: function(data) {
                $('#key_data').html('<table class="table"><thead><tr><td>Name</td><td>Description</td></tr></thead>' +
                                     '<tbody id="row_show"></tbody></table>');
                for (i = 0; i < data.length; i++) {
                    $('#row_show').append("<tr>" +
                        "<td>" + data[i][0] + "</td>" +
                        "<td>" + data[i][1] + "</td></tr>")
                }
            }
        });
    }
    keycombo_data();

//    input keyCombos
    $('#keycombo_check').makeKeyCombinator({
        onComplete: function(keyComboData){
            $.ajax ({
                url: "/keySet/",
                type: "POST",
                dataType: "json",
                data: JSON.stringify(keyComboData),
                success: function(data){
                    $('#description').html(data);
                }
            });
            console.log(keyComboData);
        }
    });

});