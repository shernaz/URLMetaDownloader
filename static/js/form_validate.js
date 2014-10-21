
// Form validation code will come here.
function validate()
{

   if( document.test.url.value == "" )
   {
     alert( "Please provide URL!" );
     document.test.url.focus() ;
     return false;
   }
   
    if( document.test.title.value == "" )
   {
     alert( "Please provide title!" );
     document.test.title.focus() ;
     return false;
   }
   
    if( document.test.meta_desc.value == "" )
   {
     alert( "Please provide Meta description!" );
     document.test.meta_desc.focus() ;
     return false;
   }
   
   
    if( document.test.meta_keyword.value == "" )
   {
     alert( "Please provide Meta keyword!" );
     document.test.meta_keyword.focus() ;
     return false;
   }
   /*if( document.myForm.EMail.value == "" )
   {
     alert( "Please provide your Email!" );
     document.myForm.EMail.focus() ;
     return false;
   }
   if( document.myForm.Zip.value == "" ||
           isNaN( document.myForm.Zip.value ) ||
           document.myForm.Zip.value.length != 5 )
   {
     alert( "Please provide a zip in the format #####." );
     document.myForm.Zip.focus() ;
     return false;
   }
   if( document.myForm.Country.value == "-1" )
   {
     alert( "Please provide your country!" );
     return false;
   }
   */
   return( true );
}
