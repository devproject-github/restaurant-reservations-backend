from django.urls                        import path
from rest_framework_simplejwt.views     import (TokenRefreshView,)

from apps.cuenta.views.ingresar                         import IngresarAPIView
from apps.cuenta.views.registrar                        import RegistraView
from apps.cuenta.views.verificar_correo                 import VerificarCorreo
from apps.cuenta.views.ver_usuario                      import ver_usuario
#from apps.cuenta.views.ver_codigo_verificacion          import ver_codigo_verificacion
from apps.cuenta.views.salir                            import SalirAPIView
from apps.cuenta.views.solicitar_reinicio_clave         import SoliciarReinicioClave
from apps.cuenta.views.confirmar_reinicio_clave         import ConfirmarReinicioClave
from apps.cuenta.views.definir_nueva_clave              import DefinirNuevaClave
from apps.cuenta.views.cambiar_clave                    import CambiarClave
from apps.cuenta.views.actualizar_preguntas_respuestas  import actualizar_preguntas_respuestas_recuperacion
from apps.cuenta.views.actualizar_correo                import actualizar_correo
#from apps.cuenta.views.verificar_usuario                import verificar_usuario
#from apps.cuenta.views.comprobar_existencia_usuario     import comprobar_existencia_usuario
from apps.cuenta.views.buscar_preguntas_recuperacion    import buscar_preguntas_recuperacion
from apps.cuenta.views.responder_preguntas_recuperacion import responder_preguntas_recuperacion
from apps.cuenta.views.cambiar_clave_recuperacion       import cambiar_clave_recuperacion
#from apps.cuenta.views.verificar_credencial             import verificar_credencial
from apps.cuenta.views.comprobar_servicio               import comprobar_servicio
from apps.cuenta.views.sing_in                          import sign_in


urlpatterns =   [
                    #path('registro/01/comprobar/',                                  comprobar_existencia_usuario,                   name = 'comprobar_existencia_usuario'       ),
                    #path('registro/02/verificar-correo/',                           VerificarCorreo.as_view(),                      name = "verificar-correo"                   ),
                    #path('registro/03/registrar/',                                  RegistraView.as_view(),                         name = "registrar"                          ),

                    path('ingresar/',                                               IngresarAPIView.as_view(),                      name = "ingresar"                           ),
                    path('ver-usuario/<int:id>/',                                   ver_usuario,                                    name = 'ver-usuario'                        ),
                    #path('ver-codigo-verificacion/<str:origen>/<int:cedula>/',      ver_codigo_verificacion,                        name = 'ver-codigo-verificacion'            ),
                    path('salir/',                                                  SalirAPIView.as_view(),                         name = "salir"                              ),
                    
                    path('refrecar-token/',                                         TokenRefreshView.as_view(),                     name = 'refrescar-token'                    ),
                    path('cambiar-clave/',                                          CambiarClave.as_view(),                         name = 'cambiar-clave'                      ),
                    path('actualizar-preguntas-respuestas/<int:id>/',               actualizar_preguntas_respuestas_recuperacion,   name = 'actualizar-preguntas-respuestas-recuperacion'   ),
                    path('actualizar-correo/<int:id>/',                             actualizar_correo,                              name = 'actualizar-correo'                  ),

                    # Recuperación de clave mediante correo
                    path('recuperar-clave-correo/01/solicitar/',                    SoliciarReinicioClave.as_view(),                 name = "solicitar-reinicio-clave"           ),
                    path('recuperar-clave-correo/02/confirmar/<uidb64>/<token>/',   ConfirmarReinicioClave.as_view(),                name = 'reiniciar-clave'                    ),
                    path('recuperar-clave-correo/03/finalizar/',                    DefinirNuevaClave.as_view(),                     name = 'definir-nueva-clave'                ),

                    # Recuperación de clave mediante preguntas/respuestas
                    path('recuperar-clave/01/buscar-preguntas/',                    buscar_preguntas_recuperacion,                   name = 'buscar-preguntas-recuperacion'      ),
                    path('recuperar-clave/02/responder-preguntas/',                 responder_preguntas_recuperacion,                name = 'responder-preguntas-recuperacion'   ),
                    path('recuperar-clave/03/cambiar-clave/',                       cambiar_clave_recuperacion,                      name = 'cambiar-clave-recuperacion'         ),

                    #path('verificar-credencial/codigo/',                           verificar_credencial,                            name = 'verificar-credencial'               ),
                    path('comprobar-servicio/',                                     comprobar_servicio,                              name = 'comprobar-servicio'            ),
                ]