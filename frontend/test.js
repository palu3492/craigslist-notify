
//load in the category->sub category JSON
let stateJSON;
$.getJSON("states_and_cities.json", function(json){
    stateJSON = json;
});
function changeCities(state){
    cities = stateJSON[state];
    city_select = $("#cities");
    city_select.empty();
    $.each(cities, function(index, value ){
        city_select.append("<option>" + value + "</option>");
    });
}

//load in the states->city JSON
let categoryJSON;
$.getJSON("categories_and_subs.json", function(json){
    categoryJSON = json;
});
function changeSubCategories(category){
    sub_categories = categoryJSON[category];
    sub_category_select = $("#sub_categories");
    sub_category_select.empty();
    //if sub category is empty then don't show it
    if(sub_categories.length == 0){
        $(sub_category_select).css("display", "none");
    } else {
        $(sub_category_select).css("display", "initial");
    }
    $.each(sub_categories, function(index, value ){
        sub_category_select.append("<option>" + value + "</option>");
    });
}

//load craigslist codes for each category and sub category
let categoryCodesJSON, subCategoryCodesJSON, cityCodesJSON;
$.getJSON("category_codes.json", function(json){
    categoryCodesJSON = json;
});
$.getJSON("sub_category_codes.json", function(json){
    subCategoryCodesJSON = json;
});
$.getJSON("city_codes.json", function(json){
    cityCodesJSON = json;
});
function createCraigslistURL(){
    query = $("#search_query").val();
    state = $("#states").val();
    city = $("#cities").val();
    city = cityCodesJSON[city];
    category = $("#categories").val();
    sub_category = $("#sub_categories").val();
    if(sub_category === "all" || sub_category === null){
        categoryCode = categoryCodesJSON[category];
    } else {
        categoryCode = subCategoryCodesJSON[sub_category];
    }

    filtersString = "";
    $("#filters1 input").each(function(i){
        if($(this).is(":checked")){
            filterName = $(this).attr("name");
            if(filterName === "srchType"){
                filtersString = filtersString.concat("&",filterName,"=T");
            }else {
                filtersString = filtersString.concat("&",filterName,"=1");
            }

        }
    });

    url = "https://" + city +".craigslist.org/search/" + categoryCode + "?query=" + query + "&sort=rel" + filtersString;
    $("#url1").attr("href", url);
    $("#url2").text(url);
}

$(document).ready(function(){

    //use the users ip to get state (location)

    changeCities("Minnesota");
    changeSubCategories("for sale");
    createCraigslistURL();

    $("#states").change(function(){
        let state = $(this).val();
        changeCities(state);
        createCraigslistURL();
    });

    $("#categories").change(function(){
        let category = $(this).val();
        changeSubCategories(category);
        createCraigslistURL();
    });

    $("#sub_categories").change(function(){
        createCraigslistURL();
    });

    $("#cities").change(function(){
        createCraigslistURL();
    });

    $("#search_query").keyup(function(){
        createCraigslistURL();
    });

    $(":checkbox").change(function(){
        createCraigslistURL();
    });

});