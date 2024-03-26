OPC_BOOL = [('S', 'Si'), ('N', 'No')]

OPC_CLASEDOC = (
    ('C', 'Cédula de Ciudadanía'),
    ('T', 'Tarjeta de Identidad'),
    ('N', 'Nit'),
    ('R', 'Registro Civil'),
    ('E', 'Cédula de Extranjería'),
    ('P', 'Pasaporte'),
    ('O', 'Otros'),
)

OPC_REGIMEN = (
    ('48', 'Responsable'),
    ('49', 'No Responsable'),
    ('Comun', 'Común'),
)

OPC_TIPTER = (
    ('N', 'Persona Natural'),
    ('J', 'Persona Jurídica'),
    ('O', 'Otro'),
)

OPC_EST_CIV = (
    ('N', 'No Aplica'),
    ('S', 'Soltero(a)'),
    ('C', 'Casado(a)'),
    ('U', 'Unión Libre'),
    ('V', 'Viudo(a)'),
    ('E', 'Separado(a)'),
    ('D', 'Divorciado(a)'),
)

OPC_PRODUCTO = (
    ('AP', 'Aportes'),
    ('AH', 'Ahorros'),
    ('CR', 'Créditos'),
    ('CC', 'Cuenta por Cobrar'),
    ('CP', 'Cuenta por Pagar'),
    ('CO', 'Contable'),
    ('BA', 'Bancos'),
)

OPC_EDUCACION = (
    ('0', 'No Aplica'),
    ('1', 'Primaria'),
    ('2', 'Bachiller'),
    ('3', 'Técnico'),
    ('4', 'Tecnólogo'),
    ('5', 'Profesional'),
    ('6', 'PosGrado'),
    ('7', 'Maestria'),
    ('8', 'Doctorado'),
    ('9', 'Otros'),
)

OPC_PARENTESCO = (
    ('0', 'No Aplica'),
    ('1', 'Esposo(a)'),
    ('2', 'Hijo(a)'),
    ('3', 'Padre o Madre'),
    ('4', 'Abuelo(a)'),
    ('5', 'Nieto(a)'),
    ('6', 'Hermano'),
    ('7', 'Hermana'),
    ('8', 'Primo(a)'),
    ('9', 'Otro Familiar'),
)

OPC_REFERENCIAS = (
    ('0', 'No Aplica'),
    ('1', 'Familiar'),
    ('2', 'Personal'),
    ('3', 'Bancaria'),
    ('4', 'Comercial'),
    ('5', 'Laboral'),
)

OPC_CANALES = (
    ('ATM', 'Red de Cajeros'),
    ('POS', 'Compras en Comercios'),
    ('IVR', 'Audio Respuesta'),
    ('TRA', 'Transferencia'),
    ('CON', 'Consignación'),
    ('EFE', 'Efectivo'),
    ('CHE', 'Cheque'),
    ('GIR', 'Giro'),
    ('WEB', 'Portal Transaccional'),
    ('MOV', 'Banca Móvil'),
    ('OFI', 'Oficina'),
    ('CNB', 'Corresponsales Bancarios'),
    ('RAL', 'Redes Aliadas')
)

OPC_NAT = (
    ('D', 'Débito'),
    ('C', 'Crédito'),
)

OPC_TERMINO = (
    ('D', 'Definido'),
    ('I', 'Indefinido'),
)

OPC_PER_LIQ_INT = (
    ('D', 'Diario'),
    ('M', 'Mensual'),
    ('C', 'Cdat'),
    ('V', 'Vencimiento'),
)

OPC_EST_CTA_AHO = (
    ('A', 'Activa'),
    ('I', 'Inactiva'),
    ('C', 'Cancelada'),
    ('E', 'Embargada'),
)

OPC_SEXO = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('N', 'No Aplica'),
)

OPC_LIQ_INT_AHO = (
    ('C', 'Causación Final'),
    ('D', 'Causación Diaria'),
    ('M', 'Causación Mensual'),
    ('V', 'Causación Vencimiento'),
    ('P', 'Pago'),
)

OPC_CRE_TERMINO = (
    ('D', 'Definido'),
    ('C', 'Cupo'),
    ('R', 'Rotativo'),
)

OPC_CRE_FOR_PAG = (
    ('P', 'Personal'),
    ('L', 'Libranza'),
)

OPC_CRE_EST_JUR = (
    ('N', 'Normal'),
    ('P', 'Persuasivo'),
    ('J', 'Cobro Jurídico'),
    ('C', 'Condonación'),
    ('T', 'Castigado'),
)

OPC_CAMBIOS_CRE = (
    ('2', 'Ajuste'),
    ('3', 'Descuento Pronto Pago'),
    ('4', 'Castigo/Condonación'),
)

OPC_CRE_CATEGORIA = (
    ('A', 'Normal'),
    ('B', 'Apreciable'),
    ('C', 'En Peligro'),
    ('D', 'En Mora'),
    ('E', 'Irrecuperable'),
    ('F', 'Castigado'),
)

OPC_EST_CRE = (
    ('X', 'Por Causar'),
    ('A', 'Activo'),
    ('C', 'Cancelado'),
    ('T', 'Terminado Cupo'),
)

OPC_MODALIDAD_CRE = (
    ('A', 'Admisible'),
    ('C', 'Comercial'),
    ('M', 'MicroCrédito'),
    ('V', 'Vivienda')
)

OPC_GARANTIA = (
    ('A', 'Admisible'),
    ('H', 'Hipotecaria'),
    ('D', 'Deudor Solidario'),
    ('O', 'Otros')
)

OPC_ESTADO_ANTEIA = (
    ('0', 'No Anteia'),
    ('1', 'Validar'),
    ('2', 'Por Validar'),
    ('3', 'Denegar')
)

OPC_TIP_CTA = (
    ('C', 'Cuenta'),
    ('A', 'Auxiliar')
)

OPC_TIP_MOV_AHO = (
    ('SALINI','Saldo Inicial Justo'),
    ('DEPOSI','Depósito'),
    ('INTCTA','Interés Cuenta'),
    ('INTCDA','Interés Cdat'),
    ('CANJE','Canje por Confirmar'),
    ('CAN_OK','Canje Confirmado'),
    ('RETIRO','Retiro'),
    ('RETFUE','Rete Fuente'),
    ('RF_CDA','Rete Fuente Cdat'),
    ('CH_DEV','Cheque Devuelto')
)