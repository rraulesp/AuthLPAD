import datetime

from ldap3 import *
from django.shortcuts import render, redirect
import ldap
import ldap.filter

from django.urls import reverse
from django.conf import settings
from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def login(request):

    if request.method == 'POST':
        user = request.POST.__getitem__('username')

        old = request.POST.__getitem__('passw')
        form=UserForm(request.POST)



        ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
        l = ldap.initialize('LDAPS://10.40.0.7:636',trace_level=3)
        l.set_option(ldap.OPT_REFERRALS,0)
        l.set_option(ldap.OPT_DEBUG_LEVEL,255)


        try:

            l.simple_bind_s(user+'@inca.edu.cu', old)


        except ldap.INVALID_CREDENTIALS:

            l.unbind_s()
            return render(request, "index.html", {"mensaje": "Usuario o Contraseña Incorrectos", "tipo":"alert-danger", 'form':form, 'error1':error})

        except:
            return render(request, "index.html", {"mensaje": "Problemas en el servidor", "tipo":"alert-danger", 'form':form, 'error1':error})



@login_required
def change_password(request):
    error='alert-validate'
    print(request.session.get('password', None), ">>password")

    if request.method == 'POST':
        password = request.session.get('password', None)
    
        user = request.user.username
        old=password
        newP = request.POST.__getitem__('passn')
        newPC = request.POST.__getitem__('passnc')
        #form=UserForm(request.POST)



        ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
        l = ldap.initialize('LDAPS://10.40.0.7:636',trace_level=3)
        l.set_option(ldap.OPT_REFERRALS,0)
        l.set_option(ldap.OPT_DEBUG_LEVEL,255)
        
        try:

            l.simple_bind_s(user+'@inca.edu.cu', old)


        except ldap.INVALID_CREDENTIALS:

            l.unbind_s()
            return render(request, "index.html", {"mensaje": "Usuario o Contraseña Incorrectos", "tipo":"alert-danger", 'error1':error})

        except:
            return render(request, "index.html", {"mensaje": "Problemas en el servidor", "tipo":"alert-danger", 'error1':error})



        if newP != newPC:
            return render(request, "index.html",
                          {"mensaje": "La nueva contraseña no coincide con la confirmada", "tipo": "alert-warning",'error':error})

        user_dn = get_dn_by_username(user, l)

        usernameAdmin=settings.AUTH_LDAP_USER+'@inca.edu.cu'
        passwordAdmin=settings.AUTH_LDAP_BIND_PASSWORD
        
        l.bind_s(usernameAdmin, passwordAdmin)

        formateadoencode='"{0}"'.format(newP) .encode('utf-16-le')

        ml = (ldap.MOD_REPLACE, "unicodePwd", formateadoencode)

        try:
            lista=[ml,ml]

            l.modify_s(user_dn,lista)
            
            l.unbind_s()


        except:
            
            return render(request, "index.html", {"mensaje": "No se pudo cambiar la contraseña", "tipo":"alert-danger"})
        
        else:
            logout(request)
            return redirect("/")
            # request.session['password'] = newP
            # return render(request, "index.html", {"mensaje": "Contraseña cambiada satisfactoriamente", "tipo":"alert-success"})
        

        
    else:
        
        return render(request, "index.html")




def get_dn_by_username(username, ad_conn, basedn="cn=users,dc=inca,dc=edu,dc=cu"):
    #ad_conn.set_option(ldap.OPT_REFERRALS, 0)
    ad_conn.protocol_version = ldap.VERSION3
    searchFilter = "sAMAccountName={}".format(username)
    searchAttribute = ["distinguishedName"]
    searchScope = ldap.SCOPE_SUBTREE


    # get result
    ldap_result= ad_conn.search_s(basedn, searchScope, searchFilter, searchAttribute)

    # extract the distinguishedName
    saMAccount = ldap_result[0][1]["distinguishedName"][0].decode('utf-8')



    return saMAccount



