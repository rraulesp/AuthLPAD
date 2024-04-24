
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType, ActiveDirectoryGroupType


# Baseline configuration.
AUTH_LDAP_SERVER_URI = 'ldap://10.40.0.7'

AUTH_LDAP_USER = "ad_search"
AUTH_LDAP_BIND_DN = 'cn=ad_search ad_search,cn=users,dc=inca,dc=edu,dc=cu'
AUTH_LDAP_BIND_PASSWORD = 'Az@7811*dz'



# Datos para autenticacion en el ldap
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    'cn=users,dc=inca,dc=edu,dc=cu',
    ldap.SCOPE_SUBTREE,
    '(samaccountname=%(user)s)',
)
# Or:
# AUTH_LDAP_USER_DN_TEMPLATE = 'uid=%(user)s,ou=users,dc=example,dc=com'

# Set up the basic group parameters.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    'dc=inca,dc=edu,dc=cu',
    ldap.SCOPE_SUBTREE,
    '(objectClass=Group)',
)
AUTH_LDAP_GROUP_TYPE = ActiveDirectoryGroupType(name_attr='cn')

# Simple group restrictions
from django_auth_ldap.config import LDAPGroupQuery
AUTH_LDAP_REQUIRE_GROUP = (
    (
        LDAPGroupQuery('CN=ARusers,OU=squid,DC=inca,DC=edu,DC=cu') |
        LDAPGroupQuery('CN=Internet,OU=squid,DC=inca,DC=edu,DC=cu') |
        LDAPGroupQuery('CN=Internet_full,OU=squid,DC=inca,DC=edu,DC=cu') |
        LDAPGroupQuery('CN=RSocial,OU=squid,DC=inca,DC=edu,DC=cu') |
        LDAPGroupQuery('CN=Video,OU=squid,DC=inca,DC=edu,DC=cu')|
        LDAPGroupQuery('CN=Admins. del dominio,CN=Users,DC=inca,DC=edu,DC=cu')

    )
)

# Simple group restrictions
# AUTH_LDAP_REQUIRE_GROUP = 'cn=enabled,ou=django,ou=groups,dc=example,dc=com'
# AUTH_LDAP_DENY_GROUP = 'cn=disabled,ou=django,ou=groups,dc=example,dc=com'

#
#
# # Populate the Django user from the LDAP directory.
# AUTH_LDAP_USER_ATTR_MAP = {
#     'first_name': 'givenName',
#     'last_name': 'sn',
#     'email': 'mail',
#     'userName' : 'sAMAccountName',
#     'phone': 'telephoneNumber',
#     'department':'department',
#     'company':'company',
#     'provincia':'st',
#     'municipio':'l',
#     'direccion':'streetAddress',
#     'carnetid' : 'employeeId',
#     # 'desc' : 'description',
#    'company' : 'company',
#    'department' : 'department',
#    'avatar' : 'thumbnailPhoto',
#    'connectioType' : 'info',
#    'mailType' : 'otherMailbox',
#    'user_tipe' : 'physicalDeliveryOfficeName',
# }

AUTH_LDAP_USER_ATTR_MAP = {
    'first_name': 'givenName',
    'last_name': 'sn',
    'email': 'mail',
    'userName': 'sAMAccountName',}

AUTH_LDAP_AUTHORIZE_ALL_USERS = True

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    'is_active': (
        'CN=ARusers,OU=squid,DC=inca,DC=edu,DC=cu',
        'CN=Internet,OU=squid,DC=inca,DC=edu,DC=cu',
        'CN=Internet_full,OU=squid,DC=inca,DC=edu,DC=cu',
       'CN=RSocial,OU=squid,DC=inca,DC=edu,DC=cu',
        'CN=Video,OU=squid,DC=inca,DC=edu,DC=cu',
    'CN=Admins. del dominio,CN=Users,DC=inca,DC=edu,DC=cu'
    ),
    'is_staff': (
        # 'CN=Admins. del dominio,CN=Users,DC=inca,DC=edu,DC=cu',
        'CN=Internet, OU=squid, DC=inca, DC=edu, DC=cu'    ),
    'is_superuser': ('CN=Admins. del dominio,cn=Users,dc=inca,dc=edu,dc=cu')
}


# # Populate the Django user from the LDAP directory.
# AUTH_LDAP_USER_ATTR_MAP = {
#     'first_name': 'givenName',
#     'last_name': 'sn',
#     'email': 'mail',
# }

# AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#     'is_active': 'cn=active,ou=django,ou=groups,dc=example,dc=com',
#     'is_staff': 'cn=staff,ou=django,ou=groups,dc=example,dc=com',
#     'is_superuser': 'cn=superuser,ou=django,ou=groups,dc=example,dc=com',
# }

# This is the default, but I like to be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# Use LDAP group membership to calculate group permissions.
AUTH_LDAP_FIND_GROUP_PERMS = True

# Cache distinguished names and group memberships for an hour to minimize
# LDAP traffic.
AUTH_LDAP_CACHE_TIMEOUT = 3600

# Keep ModelBackend around for per-user permissions and maybe a local
# superuser.
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)