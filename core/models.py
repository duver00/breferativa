# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Autores(models.Model):
    codaut = models.IntegerField(primary_key=True)
    desaut = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'autores'


class ClConceptos(models.Model):
    idconcepto = models.SmallIntegerField(primary_key=True)
    nombreconcepto = models.CharField(max_length=50, blank=True, null=True)
    descripcionconcepto = models.CharField(max_length=255, blank=True, null=True)
    obliga = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cl_conceptos'


class ClTareas(models.Model):
    idtarea = models.IntegerField(primary_key=True)
    nombretarea = models.CharField(max_length=255, blank=True, null=True)
    nomborg = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cl_tareas'


class ClTclasif(models.Model):
    cl_aidclasif = models.SmallIntegerField(primary_key=True)
    cl_anomclasif = models.CharField(max_length=30, blank=True, null=True)
    cl_anomlclasif = models.CharField(max_length=70, blank=True, null=True)
    cl_tipo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cl_tclasif'


class ClTclasifcod(models.Model):
    cl_aidclasif = models.OneToOneField(ClTclasif, models.DO_NOTHING, db_column='cl_aidclasif', primary_key=True)
    cl_aidcoditem = models.SmallIntegerField()
    cl_anomitem = models.CharField(max_length=30, blank=True, null=True)
    cl_anomlitem = models.CharField(max_length=70, blank=True, null=True)
    cl_apenditemum = models.FloatField(blank=True, null=True)
    cl_atermindum = models.FloatField(blank=True, null=True)
    vr_idvariable = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cl_tclasifcod'
        unique_together = (('cl_aidclasif', 'cl_aidcoditem'),)


class ClTclasifsinonim(models.Model):
    cl_aidclasif = models.OneToOneField(ClTclasifcod, models.DO_NOTHING, db_column='cl_aidclasif', primary_key=True)
    cl_aidcoditem = models.SmallIntegerField()
    cl_aidcodsinonim = models.SmallIntegerField()
    cl_anomsinonim = models.CharField(max_length=30, blank=True, null=True)
    cl_anomlsinonim = models.CharField(max_length=70, blank=True, null=True)
    cl_apenditemum = models.FloatField(blank=True, null=True)
    cl_atermindum = models.FloatField(blank=True, null=True)
    cl_utiliza = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cl_tclasifsinonim'
        unique_together = (('cl_aidclasif', 'cl_aidcoditem', 'cl_aidcodsinonim'),)


class CoordenadasSector(models.Model):
    inventario = models.OneToOneField('Refyac', models.DO_NOTHING, db_column='inventario', primary_key=True)
    codsector = models.IntegerField()
    novertice = models.IntegerField()
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coordenadas_sector'
        unique_together = (('inventario', 'codsector', 'novertice'),)


class DesEntidad(models.Model):
    codentidadejecutante = models.IntegerField(primary_key=True)
    desentidad = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'des_entidad'


class DesRegistrador(models.Model):
    codregistrador = models.IntegerField(primary_key=True)
    desregistrador = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'des_registrador'


class Escalas(models.Model):
    codesc = models.IntegerField(blank=True, null=True)
    desescala = models.CharField(max_length=50, blank=True, null=True)
    orden = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escalas'


class Fichas(models.Model):
    inventario = models.IntegerField(primary_key=True)
    anno = models.IntegerField(blank=True, null=True)
    titulo = models.CharField(max_length=255, blank=True, null=True)
    resumen = models.TextField(blank=True, null=True)
    codidi = models.IntegerField(blank=True, null=True)
    codentidadejecutante = models.IntegerField(blank=True, null=True)
    codregistrador = models.IntegerField(blank=True, null=True)
    base_datos = models.BooleanField(blank=True, null=True)
    dateentarchivo = models.DateTimeField(blank=True, null=True)
    clasificado = models.BooleanField(blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)
    actaonrm = models.CharField(max_length=50, blank=True, null=True)
    certificaprob = models.DateField(blank=True, null=True)
    sistref = models.IntegerField(blank=True, null=True)
    tienecoord = models.BooleanField(blank=True, null=True)
    digitalizado = models.BooleanField(blank=True, null=True)
    tieneanexotext = models.BooleanField(blank=True, null=True)
    tieneanexografico = models.BooleanField(blank=True, null=True)
    inventariocompleto = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fichas'


class Idiomas(models.Model):
    codidi = models.IntegerField(primary_key=True)
    idioma = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idiomas'


class LibroEntrada(models.Model):
    codentrada = models.IntegerField(primary_key=True)
    inventario = models.ForeignKey(Fichas, models.DO_NOTHING, db_column='inventario')
    ejemplar = models.CharField(max_length=5, blank=True, null=True)
    tomo = models.CharField(max_length=50, blank=True, null=True)
    numero_paginas = models.IntegerField(blank=True, null=True)
    dibujos = models.IntegerField(blank=True, null=True)
    anexos_graficos = models.IntegerField(blank=True, null=True)
    fotos = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'libro_entrada'
        unique_together = (('codentrada', 'inventario'),)


class Materias(models.Model):
    codmater = models.IntegerField(primary_key=True)
    materia = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materias'


class MateriasPrimas(models.Model):
    codmat = models.IntegerField(primary_key=True)
    desmat = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'materias_primas'


class Oficina(models.Model):
    codofi = models.IntegerField(primary_key=True)
    oficina = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oficina'


class Perf(models.Model):
    etiquetacapa = models.CharField(primary_key=True, max_length=50)
    tablarasgo = models.CharField(max_length=50, blank=True, null=True)
    masterfield = models.CharField(max_length=50, blank=True, null=True)
    tablacorrd = models.CharField(max_length=50, blank=True, null=True)
    llavecoord = models.CharField(max_length=50, blank=True, null=True)
    campox = models.CharField(max_length=50, blank=True, null=True)
    campoy = models.CharField(max_length=50, blank=True, null=True)
    campocota = models.CharField(max_length=50, blank=True, null=True)
    campoazimut = models.CharField(max_length=50, blank=True, null=True)
    campobuzamiento = models.CharField(max_length=50, blank=True, null=True)
    tablaregistro = models.CharField(max_length=50, blank=True, null=True)
    llaveregistro = models.CharField(max_length=50, blank=True, null=True)
    campodesde = models.CharField(max_length=50, blank=True, null=True)
    campohasta = models.CharField(max_length=50, blank=True, null=True)
    campolongitud = models.CharField(max_length=50, blank=True, null=True)
    error = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perf'


class PerfCampos(models.Model):
    etiquetacapa = models.OneToOneField(Perf, models.DO_NOTHING, db_column='etiquetacapa', primary_key=True)
    idcampo = models.SmallIntegerField()
    camporegistro = models.CharField(max_length=50, blank=True, null=True)
    plotear = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perf_campos'
        unique_together = (('etiquetacapa', 'idcampo'),)


class PerfCapas(models.Model):
    etiqueta = models.OneToOneField('PerfEtiqueta', models.DO_NOTHING, db_column='etiqueta', primary_key=True)
    idcapa = models.SmallIntegerField()
    nombrecapa = models.CharField(max_length=60, blank=True, null=True)
    shp = models.BinaryField(blank=True, null=True)
    dbf = models.BinaryField(blank=True, null=True)
    shx = models.BinaryField(blank=True, null=True)
    shl = models.BinaryField(blank=True, null=True)
    marca = models.CharField(max_length=1, blank=True, null=True)
    tipocapa = models.CharField(max_length=1, blank=True, null=True)
    etiquetaploteo = models.CharField(max_length=25, blank=True, null=True)
    prj = models.BinaryField(blank=True, null=True)
    zip = models.BinaryField(blank=True, null=True)
    shp1 = models.BinaryField(blank=True, null=True)
    shpa = models.BinaryField(blank=True, null=True)
    dbfa = models.BinaryField(blank=True, null=True)
    shlxa = models.BinaryField(blank=True, null=True)
    shla = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perf_capas'
        unique_together = (('etiqueta', 'idcapa'),)


class PerfEtiqueta(models.Model):
    etiqueta = models.CharField(primary_key=True, max_length=25)
    x1 = models.FloatField(blank=True, null=True)
    y1 = models.FloatField(blank=True, null=True)
    x2 = models.FloatField(blank=True, null=True)
    y2 = models.FloatField(blank=True, null=True)
    zmax = models.FloatField(blank=True, null=True)
    zmin = models.FloatField(blank=True, null=True)
    distmax = models.FloatField(blank=True, null=True)
    fescala = models.SmallIntegerField(blank=True, null=True)
    imarca = models.CharField(max_length=1, blank=True, null=True)
    disteperfiles = models.FloatField(blank=True, null=True)
    realizo = models.CharField(max_length=40, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    comentario = models.CharField(max_length=70, blank=True, null=True)
    xd = models.CharField(max_length=1, blank=True, null=True)
    tipocapa = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perf_etiqueta'


class PerfIntervalo(models.Model):
    etiqueta = models.OneToOneField('PerfPozo', models.DO_NOTHING, db_column='etiqueta', primary_key=True)
    poligono = models.CharField(max_length=8)
    bloque = models.CharField(max_length=4)
    pozo = models.CharField(max_length=10)
    desde = models.FloatField()
    hasta = models.FloatField()
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    y1 = models.FloatField(blank=True, null=True)
    y2 = models.FloatField(blank=True, null=True)
    mena = models.CharField(max_length=2, blank=True, null=True)
    litologia = models.SmallIntegerField(blank=True, null=True)
    fe = models.FloatField(blank=True, null=True)
    ni = models.FloatField(blank=True, null=True)
    co = models.FloatField(blank=True, null=True)
    al2o3 = models.FloatField(blank=True, null=True)
    mgo = models.FloatField(blank=True, null=True)
    sio2 = models.FloatField(blank=True, null=True)
    pv = models.FloatField(blank=True, null=True)
    eni = models.FloatField(blank=True, null=True)
    eco = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perf_intervalo'
        unique_together = (('etiqueta', 'poligono', 'bloque', 'pozo', 'desde', 'hasta'),)


class PerfLeyenda(models.Model):
    etiqueta = models.OneToOneField(PerfCapas, models.DO_NOTHING, db_column='etiqueta', primary_key=True)
    idcapa = models.SmallIntegerField()
    idley = models.SmallIntegerField()
    nombreley = models.CharField(max_length=30, blank=True, null=True)
    ecuacionley = models.CharField(max_length=250, blank=True, null=True)
    simbololey = models.IntegerField(blank=True, null=True)
    sizeley = models.SmallIntegerField(blank=True, null=True)
    pencolor = models.IntegerField(blank=True, null=True)
    penwidth = models.SmallIntegerField(blank=True, null=True)
    penstyle = models.SmallIntegerField(blank=True, null=True)
    brushstyle = models.IntegerField(blank=True, null=True)
    brushcolor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perf_leyenda'
        unique_together = (('etiqueta', 'idcapa', 'idley'),)


class PerfPozo(models.Model):
    etiqueta = models.OneToOneField(PerfEtiqueta, models.DO_NOTHING, db_column='etiqueta', primary_key=True)
    poligono = models.CharField(max_length=8)
    bloque = models.CharField(max_length=4)
    pozo = models.CharField(max_length=10)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perf_pozo'
        unique_together = (('etiqueta', 'poligono', 'bloque', 'pozo'),)


class ProvinciaCono(models.Model):
    primerodeinventario = models.IntegerField(blank=True, null=True)
    primerodeanno = models.IntegerField(blank=True, null=True)
    titulo = models.CharField(max_length=255, blank=True, null=True)
    promediodex = models.FloatField(blank=True, null=True)
    promediodey = models.FloatField(blank=True, null=True)
    primerodedesmat = models.CharField(max_length=255, blank=True, null=True)
    desyac = models.CharField(max_length=40, blank=True, null=True)
    primerodeprovincia = models.CharField(max_length=255, blank=True, null=True)
    primerodenovertice = models.IntegerField(blank=True, null=True)
    cono = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincia_cono'


class Provincias(models.Model):
    codpro = models.IntegerField(primary_key=True)
    provincia = models.CharField(max_length=20, blank=True, null=True)
    cubanorte = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'provincias'


class Qcampohistoclasif(models.Model):
    nombrebd = models.CharField(primary_key=True, max_length=15)
    nombretabla = models.CharField(max_length=50)
    orden = models.IntegerField()
    id = models.IntegerField()
    atributo = models.CharField(max_length=30, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    porciento = models.FloatField(blank=True, null=True)
    idclasif = models.IntegerField(blank=True, null=True)
    clasifnom = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qcampohistoclasif'
        unique_together = (('nombrebd', 'nombretabla', 'orden', 'id'),)


class Qcampohistonum(models.Model):
    nombrebd = models.OneToOneField('Qcamponum', models.DO_NOTHING, db_column='nombrebd', primary_key=True)
    nombretabla = models.CharField(max_length=50)
    orden = models.IntegerField()
    idcentro = models.IntegerField()
    nombrecampo = models.CharField(max_length=50, blank=True, null=True)
    desde = models.FloatField(blank=True, null=True)
    hasta = models.FloatField(blank=True, null=True)
    centro = models.FloatField(blank=True, null=True)
    ncant = models.IntegerField(blank=True, null=True)
    porciento = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qcampohistonum'
        unique_together = (('nombrebd', 'nombretabla', 'orden', 'idcentro'),)


class Qcamponum(models.Model):
    nombrebd = models.CharField(primary_key=True, max_length=15)
    nombretabla = models.CharField(max_length=50)
    orden = models.IntegerField()
    nombrecampo = models.CharField(max_length=50, blank=True, null=True)
    promedio = models.FloatField(blank=True, null=True)
    minimo = models.FloatField(blank=True, null=True)
    maximo = models.FloatField(blank=True, null=True)
    desvstd = models.FloatField(blank=True, null=True)
    minhistograma = models.FloatField(blank=True, null=True)
    nintervalos = models.IntegerField(blank=True, null=True)
    anchointervalo = models.FloatField(blank=True, null=True)
    cantnull = models.IntegerField(blank=True, null=True)
    histograma = models.BinaryField(blank=True, null=True)
    limiteinferior = models.FloatField(blank=True, null=True)
    limitesuperior = models.FloatField(blank=True, null=True)
    error = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qcamponum'
        unique_together = (('nombrebd', 'nombretabla', 'orden'),)


class Qtablaesquema(models.Model):
    nombretabla = models.CharField(primary_key=True, max_length=50)
    orden = models.CharField(max_length=50, blank=True, null=True)
    padre = models.CharField(max_length=50, blank=True, null=True)
    etiqueta = models.CharField(max_length=50, blank=True, null=True)
    imagen = models.IntegerField(blank=True, null=True)
    alto = models.IntegerField(blank=True, null=True)
    ancho = models.IntegerField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    tempnombretabla = models.CharField(max_length=50, blank=True, null=True)
    temppadre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qtablaesquema'


class Refauto(models.Model):
    inventario = models.OneToOneField(Fichas, models.DO_NOTHING, db_column='inventario', primary_key=True)
    codaut = models.ForeignKey(Autores, models.DO_NOTHING, db_column='codaut')

    class Meta:
        managed = True
        db_table = 'refauto'
        unique_together = (('inventario', 'codaut'),)


class Refeval(models.Model):
    inventario = models.OneToOneField(Fichas, models.DO_NOTHING, db_column='inventario', primary_key=True)
    codeval = models.ForeignKey('Usos', models.DO_NOTHING, db_column='codeval')

    class Meta:
        managed = False
        db_table = 'refeval'
        unique_together = (('inventario', 'codeval'),)


class Refmat(models.Model):
    inventario = models.IntegerField(primary_key=True)
    codmat = models.ForeignKey(MateriasPrimas, models.DO_NOTHING, db_column='codmat')
    codyac = models.ForeignKey('Yacimientos', models.DO_NOTHING, db_column='codyac')

    class Meta:
        managed = True
        db_table = 'refmat'
        unique_together = (('inventario', 'codmat', 'codyac'),)


class Refmater(models.Model):
    inventario = models.OneToOneField(Fichas, models.DO_NOTHING, db_column='inventario', primary_key=True)
    codmater = models.ForeignKey(Materias, models.DO_NOTHING, db_column='codmater')

    class Meta:
        managed = True
        db_table = 'refmater'
        unique_together = (('inventario', 'codmater'),)


class Refpro(models.Model):
    inventario = models.OneToOneField(Fichas, models.DO_NOTHING, db_column='inventario', primary_key=True)
    codpro = models.ForeignKey(Provincias, models.DO_NOTHING, db_column='codpro')

    class Meta:
        managed = True
        db_table = 'refpro'
        unique_together = (('inventario', 'codpro'),)


class Refyac(models.Model):
    inventario = models.OneToOneField(Fichas, models.DO_NOTHING, db_column='inventario', primary_key=True)
    codsector = models.IntegerField()
    escala = models.CharField(max_length=12, blank=True, null=True)
    nombresector = models.CharField(max_length=200, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    cono = models.IntegerField(blank=True, null=True)
    mapa = models.CharField(max_length=12, blank=True, null=True)
    codyac = models.IntegerField(blank=True, null=True)
    sistref = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'refyac'
        unique_together = (('inventario', 'codsector'),)


class SgTadministracion(models.Model):
    fechacodigo = models.DateField(blank=True, null=True)
    fechacitacion = models.DateField(blank=True, null=True)
    fechaconfiguracion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sg_tadministracion'


class TbAccionlog(models.Model):
    accion = models.SmallIntegerField(primary_key=True)
    nombre_accion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_accionlog'


class TbCampoentidad(models.Model):
    nombrebd = models.OneToOneField('TbEntidad', models.DO_NOTHING, db_column='nombrebd', primary_key=True)
    nombretabla = models.CharField(max_length=50)
    orden = models.IntegerField()
    nombrecampo = models.CharField(max_length=50, blank=True, null=True)
    etiqueta = models.CharField(max_length=50, blank=True, null=True)
    tipodato = models.CharField(max_length=50, blank=True, null=True)
    tipokey = models.CharField(max_length=2, blank=True, null=True)
    formato = models.CharField(max_length=50, blank=True, null=True)
    validacion = models.CharField(max_length=255, blank=True, null=True)
    validacionerror = models.CharField(max_length=255, blank=True, null=True)
    vervalidacion = models.BooleanField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    lugdec = models.IntegerField(blank=True, null=True)
    vdefault = models.CharField(max_length=50, blank=True, null=True)
    vargeodato = models.SmallIntegerField(blank=True, null=True)
    clasif1 = models.SmallIntegerField(blank=True, null=True)
    clasif2 = models.SmallIntegerField(blank=True, null=True)
    clasif3 = models.SmallIntegerField(blank=True, null=True)
    tablalistacod = models.CharField(max_length=50, blank=True, null=True)
    campollavelistacod = models.CharField(max_length=50, blank=True, null=True)
    camporesultlistacod = models.CharField(max_length=50, blank=True, null=True)
    campoviejo = models.CharField(max_length=50, blank=True, null=True)
    editado = models.CharField(max_length=5, blank=True, null=True)
    vargeodatoitemum = models.SmallIntegerField(blank=True, null=True)
    campovalor = models.CharField(max_length=30, blank=True, null=True)
    campovariable = models.CharField(max_length=30, blank=True, null=True)
    tipocampo = models.CharField(max_length=6, blank=True, null=True)
    configcaracter = models.CharField(max_length=10, blank=True, null=True)
    espacio = models.IntegerField(blank=True, null=True)
    imgkey = models.BinaryField(blank=True, null=True)
    tipodatolc = models.CharField(max_length=50, blank=True, null=True)
    exten = models.CharField(max_length=10, blank=True, null=True)
    metodoana = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_campoentidad'
        unique_together = (('nombrebd', 'nombretabla', 'orden'),)


class TbCampoentidadcal(models.Model):
    nombretabla = models.OneToOneField('TbEntidadcal', models.DO_NOTHING, db_column='nombretabla', primary_key=True)
    nombrecampo = models.CharField(max_length=50)
    tipodato = models.CharField(max_length=20, blank=True, null=True)
    vargeodato = models.IntegerField(blank=True, null=True)
    umgeodato = models.IntegerField(blank=True, null=True)
    metodogeodato = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_campoentidadcal'
        unique_together = (('nombretabla', 'nombrecampo'),)


class TbCampoloockup(models.Model):
    nombrebd = models.OneToOneField(TbCampoentidad, models.DO_NOTHING, db_column='nombrebd', primary_key=True)
    nombretabla = models.CharField(max_length=50)
    orden = models.IntegerField()
    campokey = models.CharField(max_length=50)
    campomostrar = models.CharField(max_length=50, blank=True, null=True)
    tipocampo = models.CharField(max_length=50, blank=True, null=True)
    tablalookup = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_campoloockup'
        unique_together = (('nombrebd', 'nombretabla', 'orden', 'campokey'),)


class TbDatoreport(models.Model):
    nom_emp = models.CharField(max_length=100, blank=True, null=True)
    nom_pro = models.CharField(max_length=100, blank=True, null=True)
    no_jfproy = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_datoreport'


class TbEntidad(models.Model):
    nombrebd = models.OneToOneField('TbMetadato', models.DO_NOTHING, db_column='nombrebd', primary_key=True)
    nombretabla = models.CharField(max_length=50)
    etiqueta = models.CharField(max_length=50, blank=True, null=True)
    padre = models.CharField(max_length=50, blank=True, null=True)
    keyvalue = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    formatocampo = models.TextField(blank=True, null=True)
    tiporasgo = models.CharField(max_length=10, blank=True, null=True)
    tablacoord = models.CharField(max_length=50, blank=True, null=True)
    formato = models.TextField(blank=True, null=True)
    idconcepto = models.SmallIntegerField(blank=True, null=True)
    visible = models.BooleanField()
    tiporasgogeodato = models.SmallIntegerField(blank=True, null=True)
    keyrelacion = models.CharField(max_length=255, blank=True, null=True)
    intref = models.BooleanField(blank=True, null=True)
    delecasc = models.BooleanField(blank=True, null=True)
    updacasc = models.BooleanField(blank=True, null=True)
    owner = models.CharField(max_length=50, blank=True, null=True)
    tipoactualizacion = models.CharField(max_length=5, blank=True, null=True)
    fsalida = models.BooleanField(blank=True, null=True)
    editado = models.CharField(max_length=2, blank=True, null=True)
    nombretablaviejo = models.CharField(max_length=50, blank=True, null=True)
    salida = models.CharField(max_length=4, blank=True, null=True)
    vergrid = models.BooleanField(blank=True, null=True)
    formularioformat = models.TextField(blank=True, null=True)
    isview = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=1, blank=True, null=True)
    rasgo = models.IntegerField(blank=True, null=True)
    rasgogeodato = models.SmallIntegerField(blank=True, null=True)
    campovalrasgo = models.CharField(max_length=50, blank=True, null=True)
    perfiltrab = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_entidad'
        unique_together = (('nombrebd', 'nombretabla'),)


class TbEntidadcal(models.Model):
    nombretabla = models.CharField(primary_key=True, max_length=50)
    tipotabla = models.CharField(max_length=1, blank=True, null=True)
    padre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_entidadcal'


class TbEp(models.Model):
    nombretabla = models.CharField(primary_key=True, max_length=50)
    etiqueta = models.CharField(max_length=50, blank=True, null=True)
    padre = models.CharField(max_length=50, blank=True, null=True)
    keyvalue = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    formatocampo = models.TextField(blank=True, null=True)
    tiporasgo = models.CharField(max_length=10, blank=True, null=True)
    tablacoord = models.CharField(max_length=50, blank=True, null=True)
    formato = models.TextField(blank=True, null=True)
    idconcepto = models.SmallIntegerField(blank=True, null=True)
    visible = models.BooleanField()
    tiporasgogeodato = models.SmallIntegerField(blank=True, null=True)
    keyrelacion = models.CharField(max_length=50, blank=True, null=True)
    intref = models.BooleanField(blank=True, null=True)
    delecasc = models.BooleanField(blank=True, null=True)
    updacasc = models.BooleanField(blank=True, null=True)
    owner = models.CharField(max_length=50, blank=True, null=True)
    tipoactualizacion = models.CharField(max_length=5, blank=True, null=True)
    fsalida = models.BooleanField(blank=True, null=True)
    editado = models.CharField(max_length=2, blank=True, null=True)
    nombretablaviejo = models.CharField(max_length=50, blank=True, null=True)
    salida = models.CharField(max_length=4, blank=True, null=True)
    vergrid = models.BooleanField(blank=True, null=True)
    formularioformat = models.TextField(blank=True, null=True)
    isview = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_ep'


class TbEpcampos(models.Model):
    nombretabla = models.OneToOneField(TbEp, models.DO_NOTHING, db_column='nombretabla', primary_key=True)
    nombrecampo = models.CharField(max_length=50)
    orden = models.IntegerField(blank=True, null=True)
    etiqueta = models.CharField(max_length=50, blank=True, null=True)
    tipodato = models.CharField(max_length=50, blank=True, null=True)
    tipokey = models.CharField(max_length=2, blank=True, null=True)
    formato = models.CharField(max_length=50, blank=True, null=True)
    validacion = models.CharField(max_length=255, blank=True, null=True)
    validacionerror = models.CharField(max_length=255, blank=True, null=True)
    vervalidacion = models.BooleanField(blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    lugdec = models.IntegerField(blank=True, null=True)
    vdefault = models.CharField(max_length=50, blank=True, null=True)
    vargeodato = models.SmallIntegerField(blank=True, null=True)
    clasif1 = models.SmallIntegerField(blank=True, null=True)
    clasif2 = models.SmallIntegerField(blank=True, null=True)
    clasif3 = models.SmallIntegerField(blank=True, null=True)
    tablalistacod = models.CharField(max_length=50, blank=True, null=True)
    campollavelistacod = models.CharField(max_length=50, blank=True, null=True)
    camporesultlistacod = models.CharField(max_length=50, blank=True, null=True)
    campoviejo = models.CharField(max_length=50, blank=True, null=True)
    editado = models.CharField(max_length=5, blank=True, null=True)
    vargeodatoitemum = models.SmallIntegerField(blank=True, null=True)
    campovalor = models.CharField(max_length=30, blank=True, null=True)
    campovariable = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_epcampos'
        unique_together = (('nombretabla', 'nombrecampo'),)


class TbExt(models.Model):
    id = models.OneToOneField('TbProgramaAsociado', models.DO_NOTHING, db_column='id', primary_key=True)
    ext = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'tb_ext'
        unique_together = (('id', 'ext'),)


class TbFecha(models.Model):
    fecha = models.DateField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tb_fecha'


class TbFechainv(models.Model):
    fecha = models.OneToOneField(TbFecha, models.DO_NOTHING, db_column='fecha', primary_key=True)
    inv = models.IntegerField()
    comentario = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_fechainv'
        unique_together = (('fecha', 'inv'),)


class TbFichero(models.Model):
    nombrebd = models.OneToOneField('TbMetadato', models.DO_NOTHING, db_column='nombrebd', primary_key=True)
    idfichero = models.CharField(max_length=50)
    fichero = models.BinaryField(blank=True, null=True)
    fechacreacion = models.DateTimeField(blank=True, null=True)
    owner = models.CharField(max_length=30, blank=True, null=True)
    etiqueta = models.CharField(max_length=255, blank=True, null=True)
    resumen = models.TextField(blank=True, null=True)
    tipoconcepto = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_fichero'
        unique_together = (('nombrebd', 'idfichero'),)


class TbFtpconfig(models.Model):
    ftp = models.CharField(max_length=15, blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    ftpfolder = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_ftpconfig'


class TbLog(models.Model):
    usuariopc = models.CharField(primary_key=True, max_length=255)
    pc = models.CharField(max_length=255)
    fecha = models.CharField(max_length=255)
    ip = models.CharField(max_length=255, blank=True, null=True)
    usuario_sistema = models.CharField(max_length=255, blank=True, null=True)
    rol = models.CharField(max_length=255, blank=True, null=True)
    modulo = models.SmallIntegerField(blank=True, null=True)
    msg = models.CharField(max_length=255, blank=True, null=True)
    inventario_actual = models.IntegerField(db_column='Inventario_actual', blank=True, null=True)  # Field name made lowercase.
    accion = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_log'
        unique_together = (('usuariopc', 'pc', 'fecha'),)


class TbLogaccion(models.Model):
    usuario_sistema = models.OneToOneField('TbLogfecha', models.DO_NOTHING, db_column='usuario_sistema', primary_key=True)
    usuariopc = models.CharField(max_length=255)
    pc = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    modulo = models.SmallIntegerField()
    fecha = models.DateField()
    hora = models.CharField(max_length=12)
    msg = models.CharField(max_length=255, blank=True, null=True)
    inventario_actual = models.IntegerField(blank=True, null=True)
    accion = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_logaccion'
        unique_together = (('usuario_sistema', 'usuariopc', 'pc', 'ip', 'modulo', 'fecha', 'hora'),)


class TbLogdetail(models.Model):
    usuariopc = models.OneToOneField('TbLogmain', models.DO_NOTHING, db_column='usuariopc', primary_key=True)
    pc = models.CharField(max_length=255)
    fecha = models.DateField()
    usuario_sistema = models.CharField(max_length=255)
    hora = models.CharField(max_length=12)
    modulo = models.SmallIntegerField(blank=True, null=True)
    msg = models.CharField(max_length=255, blank=True, null=True)
    inventario_actual = models.IntegerField(db_column='Inventario_actual', blank=True, null=True)  # Field name made lowercase.
    accion = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_logdetail'
        unique_together = (('usuariopc', 'pc', 'fecha', 'usuario_sistema', 'hora'),)


class TbLogfecha(models.Model):
    usuario_sistema = models.OneToOneField('TbLogmodulo', models.DO_NOTHING, db_column='usuario_sistema', primary_key=True)
    usuariopc = models.CharField(max_length=255)
    pc = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    modulo = models.SmallIntegerField()
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'tb_logfecha'
        unique_together = (('usuario_sistema', 'usuariopc', 'pc', 'ip', 'modulo', 'fecha'),)


class TbLogmain(models.Model):
    usuariopc = models.CharField(primary_key=True, max_length=255)
    pc = models.CharField(max_length=255)
    fecha = models.DateField()
    usuario_sistema = models.CharField(max_length=255)
    ip = models.CharField(max_length=255, blank=True, null=True)
    rol = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_logmain'
        unique_together = (('usuariopc', 'pc', 'fecha', 'usuario_sistema'),)


class TbLogmodulo(models.Model):
    usuario_sistema = models.OneToOneField('TbLogpc', models.DO_NOTHING, db_column='usuario_sistema', primary_key=True)
    usuariopc = models.CharField(max_length=255)
    pc = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    modulo = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tb_logmodulo'
        unique_together = (('usuario_sistema', 'usuariopc', 'pc', 'ip', 'modulo'),)


class TbLogpc(models.Model):
    usuario_sistema = models.OneToOneField('TbLoguser', models.DO_NOTHING, db_column='usuario_sistema', primary_key=True)
    usuariopc = models.CharField(max_length=255)
    pc = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tb_logpc'
        unique_together = (('usuario_sistema', 'usuariopc', 'pc', 'ip'),)


class TbLoguser(models.Model):
    usuario_sistema = models.CharField(primary_key=True, max_length=255)
    rol = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_loguser'


class TbMetadato(models.Model):
    nombrebd = models.OneToOneField('TbProyecto', models.DO_NOTHING, db_column='nombrebd', primary_key=True)
    titulo = models.CharField(max_length=255, blank=True, null=True)
    titulo_alternativo = models.CharField(max_length=255, blank=True, null=True)
    identificadorbd = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    idcontacto_datos = models.CharField(max_length=30, blank=True, null=True)
    email_contacto_datos = models.CharField(max_length=50, blank=True, null=True)
    linaje = models.TextField(blank=True, null=True)
    nombre_contacto_md = models.CharField(max_length=30, blank=True, null=True)
    email_contacto_md = models.CharField(max_length=50, blank=True, null=True)
    recurso_linea = models.CharField(max_length=255, blank=True, null=True)
    escala = models.CharField(max_length=50, blank=True, null=True)
    resumen = models.TextField(blank=True, null=True)
    fecha_edicion = models.DateTimeField(blank=True, null=True)
    sm = models.CharField(max_length=10, blank=True, null=True)
    tipobd = models.CharField(max_length=20, blank=True, null=True)
    servidor = models.CharField(max_length=50, blank=True, null=True)
    bd = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    ip = models.CharField(max_length=20, blank=True, null=True)
    confeccionado = models.CharField(max_length=30, blank=True, null=True)
    repesp = models.IntegerField(blank=True, null=True)
    sistref = models.IntegerField(blank=True, null=True)
    idioma = models.IntegerField(blank=True, null=True)
    formato = models.IntegerField(blank=True, null=True)
    cattema = models.IntegerField(blank=True, null=True)
    pathbd = models.CharField(max_length=255, blank=True, null=True)
    esgeo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_metadato'


class TbModulolog(models.Model):
    modulo = models.SmallIntegerField(primary_key=True)
    nombre_modulo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_modulolog'


class TbNivel(models.Model):
    id = models.IntegerField(primary_key=True)
    nivel = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    bd = models.CharField(max_length=100, blank=True, null=True)
    nombreds = models.CharField(max_length=50, blank=True, null=True)
    parent = models.CharField(max_length=50, blank=True, null=True)
    key1 = models.CharField(max_length=50, blank=True, null=True)
    key2 = models.CharField(max_length=50, blank=True, null=True)
    cl = models.CharField(max_length=1, blank=True, null=True)
    pname = models.CharField(max_length=50, blank=True, null=True)
    nivelviejo = models.CharField(max_length=50, blank=True, null=True)
    isview = models.CharField(max_length=10, blank=True, null=True)
    coord = models.CharField(max_length=1, blank=True, null=True)
    tabla = models.BooleanField(blank=True, null=True)
    rasgo = models.BooleanField(blank=True, null=True)
    informe = models.BooleanField(blank=True, null=True)
    anexog = models.BooleanField(blank=True, null=True)
    anexot = models.BooleanField(blank=True, null=True)
    formulario = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_nivel'


class TbObjdigitales(models.Model):
    inventario = models.OneToOneField(Fichas, models.DO_NOTHING, db_column='inventario', primary_key=True)
    idhijo = models.IntegerField()
    nombre = models.CharField(max_length=255, blank=True, null=True)
    ext = models.IntegerField(blank=True, null=True)
    extnombre = models.CharField(max_length=255, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    urlraiz = models.CharField(max_length=50, blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    tamano = models.IntegerField(blank=True, null=True)
    padre = models.IntegerField(blank=True, null=True)
    level = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_objdigitales'
        unique_together = (('inventario', 'idhijo'),)


class TbObjgrafico(models.Model):
    inventario = models.OneToOneField(Fichas, models.DO_NOTHING, db_column='inventario', primary_key=True)
    comentario = models.CharField(max_length=100)
    idgraph = models.IntegerField()
    urlraiz = models.CharField(max_length=40, blank=True, null=True)
    fichero = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    miniatura = models.BooleanField(blank=True, null=True)
    cajetin = models.BooleanField(blank=True, null=True)
    pdf = models.BooleanField(blank=True, null=True)
    tif = models.BooleanField(blank=True, null=True)
    tamanopdf = models.IntegerField(blank=True, null=True)
    tamanotif = models.IntegerField(blank=True, null=True)
    tamanocaj = models.IntegerField(blank=True, null=True)
    tamanomin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_objgrafico'
        unique_together = (('inventario', 'comentario', 'idgraph'),)


class TbObjtexto(models.Model):
    inventario = models.OneToOneField(Fichas, models.DO_NOTHING, db_column='inventario', primary_key=True)
    idtexto = models.IntegerField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    urlraiz = models.CharField(max_length=255, blank=True, null=True)
    fichero = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    tamano = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_objtexto'
        unique_together = (('inventario', 'idtexto'),)


class TbPicklist(models.Model):
    nombrebd = models.OneToOneField(TbCampoentidad, models.DO_NOTHING, db_column='nombrebd', primary_key=True)
    nombretabla = models.CharField(max_length=50)
    orden = models.IntegerField()
    itemidx = models.IntegerField()
    nombreitem = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_picklist'
        unique_together = (('nombrebd', 'nombretabla', 'orden', 'itemidx'),)


class TbPoligono(models.Model):
    nombrebd = models.OneToOneField(TbMetadato, models.DO_NOTHING, db_column='nombrebd', primary_key=True)
    idpoligono = models.IntegerField()
    nombrepoligono = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_poligono'
        unique_together = (('nombrebd', 'idpoligono'),)


class TbProgramaAsociado(models.Model):
    id = models.IntegerField(primary_key=True)
    nombreprogram = models.CharField(max_length=30, blank=True, null=True)
    img = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_programa_asociado'


class TbProyInforme(models.Model):
    nombrebd = models.OneToOneField('TbProyecto', models.DO_NOTHING, db_column='nombrebd', primary_key=True)
    idinforme = models.CharField(max_length=50)
    informe = models.BinaryField(blank=True, null=True)
    fechacreacion = models.DateTimeField(blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    etiqueta = models.CharField(max_length=255, blank=True, null=True)
    resumen = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_proy_informe'
        unique_together = (('nombrebd', 'idinforme'),)


class TbProyObj(models.Model):
    nombrebd = models.OneToOneField(TbProyInforme, models.DO_NOTHING, db_column='nombrebd', primary_key=True)
    idinforme = models.CharField(max_length=50)
    idobjeto = models.CharField(max_length=50)
    objeto = models.BinaryField(blank=True, null=True)
    fechacreacion = models.DateTimeField(blank=True, null=True)
    owner = models.CharField(max_length=50, blank=True, null=True)
    etiqueta = models.CharField(max_length=255, blank=True, null=True)
    resumen = models.TextField(blank=True, null=True)
    tipoconcepto = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_proy_obj'
        unique_together = (('nombrebd', 'idinforme', 'idobjeto'),)


class TbProyecto(models.Model):
    nombrebd = models.CharField(primary_key=True, max_length=15)
    etiqueta = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fechaini = models.DateTimeField(blank=True, null=True)
    fechafin = models.DateTimeField(blank=True, null=True)
    idproyonrm = models.IntegerField(blank=True, null=True)
    owner = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_proyecto'


class TbPuedomigrar(models.Model):
    estadobd = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_puedomigrar'


class TbQuery(models.Model):
    nombrebd = models.OneToOneField(TbEntidad, models.DO_NOTHING, db_column='nombrebd', primary_key=True)
    nombretabla = models.CharField(max_length=50)
    idquery = models.SmallIntegerField()
    nombrequery = models.CharField(max_length=100, blank=True, null=True)
    codigosql = models.BinaryField(blank=True, null=True)
    sql = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_query'
        unique_together = (('nombrebd', 'nombretabla', 'idquery'),)


class TbRepcampotabla(models.Model):
    idtabla = models.OneToOneField('TbReptabla', models.DO_NOTHING, db_column='idtabla', primary_key=True)
    idcampotabla = models.IntegerField()
    nombrecampo = models.CharField(max_length=255)
    tipodato = models.CharField(max_length=255, blank=True, null=True)
    etiqueta = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    pkid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_repcampotabla'
        unique_together = (('idtabla', 'idcampotabla'),)


class TbReport(models.Model):
    id = models.IntegerField(primary_key=True)
    etiqueta = models.CharField(max_length=50, blank=True, null=True)
    namefile = models.CharField(max_length=50, blank=True, null=True)
    obj = models.BinaryField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)
    tablaasociada = models.CharField(max_length=50, blank=True, null=True)
    espacio = models.IntegerField(blank=True, null=True)
    prop = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_report'


class TbReporttabla(models.Model):
    id = models.OneToOneField(TbReport, models.DO_NOTHING, db_column='id', primary_key=True)
    nombretabla = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    cmd = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_reporttabla'
        unique_together = (('id', 'nombretabla'),)


class TbReptabla(models.Model):
    idtabla = models.IntegerField(primary_key=True)
    nombretabla = models.CharField(max_length=255)
    etiqueta = models.CharField(max_length=255, blank=True, null=True)
    pkid = models.CharField(max_length=255, blank=True, null=True)
    fk = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    idpadre = models.IntegerField(blank=True, null=True)
    nombrepadre = models.CharField(max_length=255, blank=True, null=True)
    etiquetapadre = models.CharField(max_length=255, blank=True, null=True)
    idnivel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_reptabla'


class TbRol(models.Model):
    idrol = models.SmallIntegerField(primary_key=True)
    rol = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_rol'


class TbSistref(models.Model):
    id = models.IntegerField(primary_key=True)
    sistemaref = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_sistref'


class TbSys(models.Model):
    idcont = models.IntegerField(primary_key=True)
    treecont = models.IntegerField(blank=True, null=True)
    contreport = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_sys'


class TbTareasrealiza(models.Model):
    inventario = models.OneToOneField(Fichas, models.DO_NOTHING, db_column='inventario', primary_key=True)
    task = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tb_tareasrealiza'
        unique_together = (('inventario', 'task'),)


class TbUser(models.Model):
    nombreuser = models.CharField(primary_key=True, max_length=100)
    nombreluser = models.CharField(max_length=255, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=32, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    empresa = models.CharField(max_length=255, blank=True, null=True)
    ministerio = models.CharField(max_length=255, blank=True, null=True)
    habilitado = models.CharField(max_length=1, blank=True, null=True)
    rol = models.ForeignKey(TbRol, models.DO_NOTHING, db_column='rol', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_user'


class TbValidacion(models.Model):
    idmodulo = models.OneToOneField('TbValidacionmaster', models.DO_NOTHING, db_column='idmodulo', primary_key=True)
    id = models.IntegerField()
    tabla = models.CharField(max_length=20, blank=True, null=True)
    campo = models.CharField(max_length=20, blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=15, blank=True, null=True)
    iderror = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_validacion'
        unique_together = (('idmodulo', 'id'),)


class TbValidacionmaster(models.Model):
    idmodulo = models.IntegerField(primary_key=True)
    etiqueta = models.CharField(max_length=40)
    comentario = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_validacionmaster'


class TbVertanex(models.Model):
    nombrebd = models.OneToOneField(TbProyObj, models.DO_NOTHING, db_column='nombrebd', primary_key=True)
    idinforme = models.CharField(max_length=50)
    idobjeto = models.CharField(max_length=50)
    idvertice = models.IntegerField()
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_vertanex'
        unique_together = (('nombrebd', 'idinforme', 'idobjeto', 'idvertice'),)


class TbVertices(models.Model):
    nombrebd = models.OneToOneField(TbPoligono, models.DO_NOTHING, db_column='nombrebd', primary_key=True)
    idpoligono = models.IntegerField()
    idvertice = models.IntegerField()
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_vertices'
        unique_together = (('nombrebd', 'idpoligono', 'idvertice'),)


class TbVertinformes(models.Model):
    nombrebd = models.OneToOneField(TbProyInforme, models.DO_NOTHING, db_column='nombrebd', primary_key=True)
    idinforme = models.CharField(max_length=50)
    idvertice = models.IntegerField()
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_vertinformes'
        unique_together = (('nombrebd', 'idinforme', 'idvertice'),)


class Usos(models.Model):
    codeval = models.IntegerField(primary_key=True)
    evaluacion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usos'


class VrTespecialidad(models.Model):
    vr_idespecialidad = models.SmallIntegerField(primary_key=True)
    vr_nomespecialidad = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vr_tespecialidad'


class VrTrasgo(models.Model):
    vr_idrasgo = models.SmallIntegerField(primary_key=True)
    vr_descripcion = models.CharField(max_length=30, blank=True, null=True)
    vr_tipo = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vr_trasgo'


class VrTtiporasgo(models.Model):
    vr_idrasgo = models.OneToOneField(VrTrasgo, models.DO_NOTHING, db_column='vr_idrasgo', primary_key=True)
    vr_idtiporasgo = models.SmallIntegerField()
    vr_nomtiporasgo = models.CharField(max_length=30, blank=True, null=True)
    vr_descripcion = models.TextField(blank=True, null=True)
    fuente = models.CharField(max_length=15, blank=True, null=True)
    asciifuente = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vr_ttiporasgo'
        unique_together = (('vr_idrasgo', 'vr_idtiporasgo'),)


class VrTvarelemen(models.Model):
    vr_idelemen = models.SmallIntegerField(primary_key=True)
    vr_esum = models.CharField(max_length=1, blank=True, null=True)
    vr_nomelemen = models.CharField(max_length=10, blank=True, null=True)
    vr_nomlelemen = models.CharField(max_length=30, blank=True, null=True)
    vr_descelemen = models.CharField(max_length=70, blank=True, null=True)
    vr_tipovar = models.SmallIntegerField(blank=True, null=True)
    vr_idclasif = models.SmallIntegerField(blank=True, null=True)
    vr_obligatoria = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vr_tvarelemen'


class VrTvarelemen2(models.Model):
    vr_idespecialidad = models.OneToOneField('VrTvariables', models.DO_NOTHING, db_column='vr_idespecialidad', primary_key=True)
    vr_idvariable = models.SmallIntegerField()
    vr_idvarelemen = models.ForeignKey(VrTvarelemen, models.DO_NOTHING, db_column='vr_idvarelemen')
    vr_varobligatoria = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vr_tvarelemen2'
        unique_together = (('vr_idespecialidad', 'vr_idvariable', 'vr_idvarelemen'),)


class VrTvariables(models.Model):
    vr_idespecialidad = models.OneToOneField(VrTespecialidad, models.DO_NOTHING, db_column='vr_idespecialidad', primary_key=True)
    vr_idvariable = models.SmallIntegerField()
    vr_nomvariable = models.CharField(max_length=30, blank=True, null=True)
    vr_nomlvariable = models.CharField(max_length=70, blank=True, null=True)
    vr_etiqueta = models.CharField(max_length=10, blank=True, null=True)
    vr_tipovariable = models.SmallIntegerField(blank=True, null=True)
    vr_idclasif = models.SmallIntegerField(blank=True, null=True)
    vr_obligatoria = models.CharField(max_length=1, blank=True, null=True)
    cl_aidcodsinonim = models.SmallIntegerField(blank=True, null=True)
    vr_idclasif2 = models.SmallIntegerField(blank=True, null=True)
    vr_idclasif3 = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vr_tvariables'
        unique_together = (('vr_idespecialidad', 'vr_idvariable'),)


class VrTvarrasgo(models.Model):
    vr_idrasgo = models.OneToOneField(VrTrasgo, models.DO_NOTHING, db_column='vr_idrasgo', primary_key=True)
    vr_idvarrasgo = models.SmallIntegerField()
    vr_obligatoriarasgo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vr_tvarrasgo'
        unique_together = (('vr_idrasgo', 'vr_idvarrasgo'),)


class VrTvartiporasgo(models.Model):
    vr_idrasgo = models.OneToOneField(VrTtiporasgo, models.DO_NOTHING, db_column='vr_idrasgo', primary_key=True)
    vr_idtiporasgo = models.SmallIntegerField()
    vr_idvartiporasgo = models.SmallIntegerField()
    vr_obligatoriatiporasgo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vr_tvartiporasgo'
        unique_together = (('vr_idrasgo', 'vr_idtiporasgo', 'vr_idvartiporasgo'),)


class Yacimientos(models.Model):
    codyac = models.IntegerField(primary_key=True)
    desyac = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yacimientos'
