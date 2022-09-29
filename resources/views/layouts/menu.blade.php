<aside class="main-sidebar sidebar-dark-primary elevation-4">
    <!-- Brand Logo -->
    <a href="/" class="brand-link">
        <img src="adminlte/dist/img/AdminLTELogo.png" alt="AdminLTE Logo" class="brand-image img-circle elevation-3" style="opacity: .8">
        <span class="brand-text font-weight-light">VentasRGR</span>
    </a>

    <!-- Sidebar -->
    <div class="sidebar">
        <!-- USUARIO EN MENU -->
        <!-- <div class="user-panel mt-3 pb-3 mb-3 d-flex">
            <div class="image">
                <img src="adminlte/dist/img/avatar.png" class="img-circle elevation-2" alt="User Image">
            </div>
            <div class="info">
                <div class="text-secondary">Usuario</div>
                <a href="#" class="d-block"></a>
            </div>
        </div> -->

        <!-- ***********************
                Sidebar Menu 
             ***********************-->
        <nav class="mt-2">
            <ul class="nav nav-pills nav-sidebar flex-column" data-widget="treeview" role="menu" data-accordion="false">
                <!-- Add icons to the links using the .nav-icon class
                with font-awesome or any other icon font library -->
                <li class="nav-item">
                    <a href="#" class="nav-link">
                        <i class="nav-icon fa fa-home"></i>
                        <p>
                            Dashboard
                            <i class=""></i>
                        </p>
                    </a>
                </li>


                <li class="nav-item">
                    <a href="#" class="nav-link">
                        <i class="nav-icon fas fa-chart-line"></i>
                        <p>
                            Reportes
                            <i class="right fas fa-angle-left"></i>
                        </p>
                    </a>
                    <ul class="nav nav-treeview">
                        <li class="nav-item">                            
                            <a href="#" class="nav-link">
                                <i class="fa fa-file nav-icon"></i>
                                <p>Reporte por dia</p>
                            </a>                            
                        </li>

                        <li class="nav-item">                            
                            <a href="#" class="nav-link">
                                <i class="fa fa-file nav-icon"></i>
                                <p>Reporte por fecha</p>
                            </a>                            
                        </li>
                    </ul>
                </li>

                <li class="nav-item">
                    <a href="" class="nav-link">
                        <i class="nav-icon fa fa-cart-plus"></i>
                        <p>
                            Compras
                            <i class=""></i>
                        </p>
                    </a>
                </li>

                <li class="nav-item">
                    <a href="#" class="nav-link">
                        <i class="nav-icon fas fa-shopping-cart"></i>
                        <p>
                            Ventas
                            <i class=""></i>
                        </p>
                    </a>
                </li>

                <li class="nav-item">
                    <a href="#" class="nav-link">
                        <i class="nav-icon fas fa-shipping-fast"></i>
                        <p>
                            Pedidos
                            <i class=""></i>
                        </p>
                    </a>
                </li>


                <li class="nav-item">
                    <a href="#" class="nav-link">
                        <i class="nav-icon fas fa-boxes"></i>
                        <p>
                            Inventarios
                            <i class="right fas fa-angle-left"></i>
                        </p>
                    </a>
                    <ul class="nav nav-treeview">
                        <li class="nav-item">                            
                            <a href="{{ route('categories.index') }}" class="nav-link">
                                <i class="fa fa-sitemap nav-icon"></i>
                                <p>Categorias</p>
                            </a>                           
                        </li>

                        <li class="nav-item">                            
                            <a href="" class="nav-link">
                                <i class="fa fa-shopping-bag nav-icon"></i>
                                <p>Productos</p>
                            </a>                            
                        </li>

                    </ul>
                </li>

                <li class="nav-item">
                    <a href="" class="nav-link">
                        <i class="nav-icon fas fa-users"></i>
                        <p>
                            Clientes
                            <i class=""></i>
                        </p>
                    </a>
                </li>

                <li class="nav-item">
                    <a href="" class="nav-link">
                        <i class="nav-icon fas fa-truck"></i>
                        <p>
                            Proveedores
                            <i class=""></i>
                        </p>
                    </a>
                </li>

                
                <li class="nav-item">
                    <a href="#" class="nav-link">
                        <i class="nav-icon fa fa-user-tag"></i>
                        <p>
                            Usuarios
                            <i class="right fas fa-angle-left"></i>
                        </p>
                    </a>
                    <ul class="nav nav-treeview">
                        <li class="nav-item">                            
                            <a href="" class="nav-link">
                                <i class="fa fa-user nav-icon"></i>
                                <p> Usuarios</p>
                            </a>                            
                        </li>

                        <li class="nav-item">                            
                            <a href="#" class="nav-link">
                                <i class="fa fa-check nav-icon"></i>
                                <p> Roles</p>
                            </a>                           
                        </li>
                    </ul>
                </li>

                <li class="nav-item">
                    <a href="#" class="nav-link">
                        <i class="nav-icon fa fa-cogs"></i>
                        <p>
                            Configuracion
                            <i class="right fas fa-angle-left"></i>
                        </p>
                    </a>
                    <ul class="nav nav-treeview">
                        <li class="nav-item">                            
                            <a href="" class="nav-link">
                                <i class="fa fa-building nav-icon"></i>
                                <p> Empresa</p>
                            </a>                            
                        </li>

                        <li class="nav-item">                            
                            <a href="#" class="nav-link">
                                <i class="fa fa-print nav-icon"></i>
                                <p> Impresoras</p>
                            </a>                           
                        </li>
                    </ul>
                </li>

                <li class="nav-item">
                    <a href="https://www.youtube.com/channel/UCMWSlUcDJS00-5pmicciZ_w" class="nav-link">
                        <i class="nav-icon fab fa-youtube"></i>
                        <p>
                            YouTube
                            <i class=""></i>
                        </p>
                    </a>
                </li>



            </ul>
        </nav>
    </div>
</aside>


