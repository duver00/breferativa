$(".card").click(function()
{
  $(this).toggleClass("transform-active");
  $(".disappear", this).toggleClass("appear");
});

/*$(".card").click(function()
{
  // Reset all cards
  $(".card").each(function()
  {
     $(this).removeClass("transform-active");
     $(this).addClass("transform");

     // Reset their children with class "appear" as well
     $(this).children(".appear").each(function()
     {
       $(this).removeClass("appear");
       $(this).addClass("disappear");
     });

     // Now set transform-active to the clicked card ...
     $(this).addClass("transform-active");
     $(this).removeClass("transform");

     // ... and all of its children with class "disappear" as well
     $(this).children(".disappear").each(function()
     {
       $(this).addClass("appear");
       $(this).removeClass("disappear");
     });
   });
});*/

/*
$('.card').each(function(){
  $(this).removeClass('transform-active');
});

var previous;

$(".card").click(function(){
  if(previous) 
    $(previous).removeClass("transform-active");
    $(".disappear", this).removeClass("appear");

  if(previous !== this) 
    $(this).addClass("transform-active");
    $(".disappear", this).toggleClass("appear");

  previous = this;
});*/