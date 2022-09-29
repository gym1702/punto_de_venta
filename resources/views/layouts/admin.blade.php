<!DOCTYPE html>

<html lang="es">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>@yield('titulo')</title>

  <!-- Google Font: Source Sans Pro -->
  <link rel="scriptsheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback">
  <!-- Font Awesome Icons -->
  {!! Html::style('adminlte/plugins/fontawesome-free/css/all.min.css') !!}
  <!-- SweetAlert2 -->
  {!! Html::style('adminlte/plugins/sweetalert2-theme-bootstrap-4/bootstrap-4.min.css') !!}
  <!-- Toastr -->
  {!! Html::style('adminlte/plugins/toastr/toastr.min.css') !!}
  <!-- DataTables -->
  {!! Html::style('adminlte/plugins/datatables-bs4/css/dataTables.bootstrap4.min.css') !!}
  {!! Html::style('adminlte/plugins/datatables-responsive/css/responsive.bootstrap4.min.css') !!}
  {!! Html::style('adminlte/plugins/datatables-buttons/css/buttons.bootstrap4.min.css') !!}
  <!-- XDSoft DateTimePicker -->
  <link rel="scriptsheet" href="https://cdnjs.cloudflare.com/ajax/libs/jquery-datetimepicker/2.5.20/jquery.datetimepicker.min.css" integrity="sha256-DOS9W6NR+NFe1fUhEE0PGKY/fubbUCnOfTje2JMDw3Y=" crossorigin="anonymous" />
  <!-- Theme script -->
  {!! Html::style('adminlte/dist/css/adminlte.min.css') !!}




</head>

<body class="hold-transition sidebar-mini ">

  <div class="wrapper">

  </div>

  @if(Auth::user())

    @include('layouts.cabecera')

    @include('layouts.menu')

    @yield('contenido')

  @else

    @yield('content')

  @endif


  <footer class="main-footer">
    <div class="float-right d-none d-sm-inline">
      
    </div>
    <strong>Copyright &copy; 2022 <a href="https://adminlte.io"></a>.</strong>
  </footer>



  <!-- REQUIRED SCRIPTS -->
  <!-- jQuery -->
  {!! Html::script('adminlte/plugins/jquery/jquery.min.js') !!}
  <!-- DateTimePicker -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-datetimepicker/2.5.20/jquery.datetimepicker.full.min.js" integrity="sha256-FEqEelWI3WouFOo2VWP/uJfs1y8KJ++FLh2Lbqc8SJk=" crossorigin="anonymous"></script>
  <!-- Bootstrap 4 -->
  {!! Html::script('adminlte/plugins/bootstrap/js/bootstrap.bundle.min.js') !!}
  <!-- SweetAlert2 -->
  {!! Html::script('adminlte/plugins/sweetalert2/sweetalert2.min.js') !!}
  <!-- Toastr -->
  {!! Html::script('adminlte/plugins/toastr/toastr.min.js') !!}
  <!-- DataTables  & Plugins -->
  {!! Html::script('adminlte/plugins/datatables/jquery.dataTables.min.js') !!}
  {!! Html::script('adminlte/plugins/datatables-bs4/js/dataTables.bootstrap4.min.js') !!}
  {!! Html::script('adminlte/plugins/datatables-responsive/js/dataTables.responsive.min.js') !!}
  {!! Html::script('adminlte/plugins/datatables-responsive/js/responsive.bootstrap4.min.js') !!}
  {!! Html::script('adminlte/plugins/datatables-buttons/js/dataTables.buttons.min.js') !!}
  {!! Html::script('adminlte/plugins/datatables-buttons/js/buttons.bootstrap4.min.js') !!}
  {!! Html::script('adminlte/plugins/jszip/jszip.min.js') !!}
  {!! Html::script('adminlte/plugins/pdfmake/pdfmake.min.js') !!}
  {!! Html::script('adminlte/plugins/pdfmake/vfs_fonts.js') !!}
  {!! Html::script('adminlte/plugins/datatables-buttons/js/buttons.html5.min.js') !!}
  {!! Html::script('adminlte/plugins/datatables-buttons/js/buttons.print.min.js') !!}
  {!! Html::script('adminlte/plugins/datatables-buttons/js/buttons.colVis.min.js') !!}
  <!-- AdminLTE App -->
  {!! Html::script('adminlte/dist/js/adminlte.min.js') !!}

   


  @yield('scripts')

  <!-- MUESTRA IMAGEN SELECCIONADA AL CREAR-->
  <script>
    $(document).ready(function(e) {
      $('#imagen').change(function() {
        let reader = new FileReader();
        reader.onload = (e) => {
          $('#imagenSeleccionada').attr('src', e.target.result);
        }
        reader.readAsDataURL(this.files[0]);
      });
    });
  </script>


  <!-- MUESTRA IMAGEN SELECCIONADA AL EDITAR-->
  <script>
    $(document).ready(function(e) {
      $('#picture').change(function() {
        let reader = new FileReader();
        reader.onload = (e) => {
          $('#pictureSeleccionada').attr('src', e.target.result);
        }
        reader.readAsDataURL(this.files[0]);
      });
    });
  </script>


  <!-- MENSAJES SWEETALERT DE SUCCESS -->
  @if(session('registrado') == 'Si')
  <script type="text/javascript">
    Swal.fire({
      position: 'center',
      icon: 'success',
      title: 'Registro creado con exito',
      showConfirmButton: false,
      timer: 1700
    })
  </script>
  @elseif(session('actualizado') == 'Si')
  <script type="text/javascript">
    Swal.fire({
      position: 'center',
      icon: 'success',
      title: 'Registro actualizado con exito',
      showConfirmButton: false,
      timer: 1700
    })
  </script>


  @endif



</body>

</html>