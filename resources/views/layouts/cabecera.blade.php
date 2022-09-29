<nav class="main-header navbar navbar-expand navbar-white navbar-light">
    <!-- Left navbar links -->
    <ul class="navbar-nav">
        <li class="nav-item">
            <a class="nav-link" data-widget="pushmenu" href="#" role="button"><i class="fas fa-bars"></i></a>
        </li>
    </ul>

    <!-- Right navbar links -->
    <ul class="navbar-nav ml-auto">
        <li class="nav-item">

        </li>

        <li class="nav-item">
            <a class="nav-link" data-widget="fullscreen" href="#" role="button">
                <i class="fas fa-expand-arrows-alt"></i>
            </a>
        </li>

        <li class="nav-item">
            <a class="nav-link" data-toggle="dropdown" href="#">
                
                <img src="adminlte/dist/img/avatar.png" class="img-circle elevation-2 img-sm" alt="User Image">&nbsp;
                
                {{Auth::user()->name}}
                
            </a>

            <div class="dropdown-menu dropdown-menu-lg dropdown-menu-right">

                <a href="#" class="dropdown-item">
                    <i class="fas fa-envelope mr-2"></i> Mis datos
                </a>

                <a href="{{route('logout')}}" onclick="event.preventDefault(); 
                    document.getElementById('logout-form').submit();" class="dropdown-item">
                    <i class="fas fa-envelope mr-2"></i> Salir
                </a>
                <form method="post" id="logout-form" action="{{route('logout')}}">
                    @csrf
                </form>

            </div>
        </li>
    </ul>
</nav>