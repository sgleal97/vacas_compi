
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocORnonassocXORnonassocANDnonassocNOTnonassocBORnonassocBXORnonassocBANDnonassocBNOTnonassocSHIFTISHIFTDnonassocIGUALQNIGUALQnonassocMENORQMAYORQMENORIGUALQMAYORIGUALQnonassocMASMENOSnonassocPORDIVIDIDORESIDUOABS AND ARRAY BAND BNOT BOR BXOR CADENA CHAR CORDER CORIZQ DECIMAL DIVIDIDO DOSPUNTOS ENTERO EXIT FLOAT GOTO ID IF IGUAL IGUALQ INT MAIN MAS MAYORIGUALQ MAYORQ MENORIGUALQ MENORQ MENOS NIGUALQ NOT OR PARDER PARIZQ POR PRINT PTCOMA READ RESIDUO SHIFTD SHIFTI UNSET VAR XORinit                   : MAIN DOSPUNTOS instruccionesinstrucciones          : instruccion instrucciones2instrucciones2         : instruccion instrucciones2instrucciones2         : emptyinstruccion            : asignacioninstruccion            : array_instrinstruccion            : unset_instrinstruccion            : print_instrinstruccion            : if_instrinstruccion            : etiqueta_instrinstruccion            : goto_instrinstruccion             : exit_instrinstruccion            : error PTCOMA\n                            | error DOSPUNTOSasignacion           : VAR IGUAL exp_numerica PTCOMA\n                            | VAR IGUAL READ PARIZQ  PARDER PTCOMA\n                            | VAR IGUAL BAND VAR PTCOMAarray_instr            : VAR indices IGUAL exp_numerica PTCOMAprint_instr            : PRINT PARIZQ exp_numerica PARDER PTCOMAunset_instr            : UNSET PARIZQ exp_numerica PARDER PTCOMAif_instr               : IF PARIZQ exp_numerica PARDER goto_instretiqueta_instr         : ID DOSPUNTOSgoto_instr             : GOTO ID PTCOMAexit_instr             : EXIT PTCOMAexp_numerica           : valores exp_numerica2exp_numerica         : BNOT valores\n                            | MENOS valores\n                            | NOT valoresexp_numerica           : ARRAY PARIZQ PARDERexp_numerica           : ABS PARIZQ valores PARDERexp_numerica           : PARIZQ tipo_dato PARDER VARexp_numerica2          : signo valoresexp_numerica2          : emptyindices                : indice indices2indices2               : indice indices2indices2               : emptyindice                 : CORIZQ exp_numerica CORDERvalores          : ENTEROvalores           : DECIMALvalores                : VARvalores                : VAR indicesvalores                : CADENAsigno                : MAS\n                            | MENOS\n                            | POR\n                            | DIVIDIDO\n                            | RESIDUO\n                            | AND\n                            | OR\n                            | XOR\n                            | BAND\n                            | BOR\n                            | BXOR\n                            | SHIFTI\n                            | SHIFTD\n                            | IGUALQ\n                            | NIGUALQ\n                            | MAYORQ\n                            | MENORQ\n                            | MAYORIGUALQ\n                            | MENORIGUALQtipo_dato              : INTtipo_dato              : FLOATtipo_dato              : CHARempty                  :'
    
_lr_action_items = {'MAIN':([0,],[2,]),'$end':([1,4,5,6,7,8,9,10,11,12,13,22,23,24,25,26,34,36,37,60,62,104,108,109,110,111,112,],[0,-1,-65,-5,-6,-7,-8,-9,-10,-11,-12,-65,-2,-4,-13,-14,-22,-24,-3,-23,-15,-17,-18,-20,-19,-21,-16,]),'DOSPUNTOS':([2,14,19,],[3,26,34,]),'error':([3,5,6,7,8,9,10,11,12,13,22,25,26,34,36,60,62,104,108,109,110,111,112,],[14,14,-5,-6,-7,-8,-9,-10,-11,-12,14,-13,-14,-22,-24,-23,-15,-17,-18,-20,-19,-21,-16,]),'VAR':([3,5,6,7,8,9,10,11,12,13,22,25,26,27,30,31,32,33,34,36,42,44,45,46,52,60,62,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,103,104,108,109,110,111,112,],[15,15,-5,-6,-7,-8,-9,-10,-11,-12,15,-13,-14,38,38,38,38,38,-22,-24,68,38,38,38,38,-23,-15,38,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,38,113,-17,-18,-20,-19,-21,-16,]),'UNSET':([3,5,6,7,8,9,10,11,12,13,22,25,26,34,36,60,62,104,108,109,110,111,112,],[16,16,-5,-6,-7,-8,-9,-10,-11,-12,16,-13,-14,-22,-24,-23,-15,-17,-18,-20,-19,-21,-16,]),'PRINT':([3,5,6,7,8,9,10,11,12,13,22,25,26,34,36,60,62,104,108,109,110,111,112,],[17,17,-5,-6,-7,-8,-9,-10,-11,-12,17,-13,-14,-22,-24,-23,-15,-17,-18,-20,-19,-21,-16,]),'IF':([3,5,6,7,8,9,10,11,12,13,22,25,26,34,36,60,62,104,108,109,110,111,112,],[18,18,-5,-6,-7,-8,-9,-10,-11,-12,18,-13,-14,-22,-24,-23,-15,-17,-18,-20,-19,-21,-16,]),'ID':([3,5,6,7,8,9,10,11,12,13,20,22,25,26,34,36,60,62,104,108,109,110,111,112,],[19,19,-5,-6,-7,-8,-9,-10,-11,-12,35,19,-13,-14,-22,-24,-23,-15,-17,-18,-20,-19,-21,-16,]),'GOTO':([3,5,6,7,8,9,10,11,12,13,22,25,26,34,36,60,62,101,104,108,109,110,111,112,],[20,20,-5,-6,-7,-8,-9,-10,-11,-12,20,-13,-14,-22,-24,-23,-15,20,-17,-18,-20,-19,-21,-16,]),'EXIT':([3,5,6,7,8,9,10,11,12,13,22,25,26,34,36,60,62,104,108,109,110,111,112,],[21,21,-5,-6,-7,-8,-9,-10,-11,-12,21,-13,-14,-22,-24,-23,-15,-17,-18,-20,-19,-21,-16,]),'PTCOMA':([14,21,29,35,38,39,43,49,50,51,53,54,55,61,68,69,71,91,92,93,96,97,98,99,100,102,105,106,113,114,],[25,36,-65,60,-40,62,-65,-38,-39,-42,-65,-34,-36,-41,104,-25,-33,-26,-27,-28,108,-35,-37,109,110,112,-32,-29,-31,-30,]),'IGUAL':([15,28,29,53,54,55,97,98,],[27,52,-65,-65,-34,-36,-35,-37,]),'CORIZQ':([15,29,38,53,98,],[30,30,30,30,-37,]),'PARIZQ':([16,17,18,27,30,31,32,33,40,47,48,52,],[31,32,33,41,41,41,41,41,63,94,95,41,]),'READ':([27,],[40,]),'BAND':([27,29,38,43,49,50,51,53,54,55,61,97,98,],[42,-65,-40,80,-38,-39,-42,-65,-34,-36,-41,-35,-37,]),'BNOT':([27,30,31,32,33,52,],[44,44,44,44,44,44,]),'MENOS':([27,29,30,31,32,33,38,43,49,50,51,52,53,54,55,61,97,98,],[45,-65,45,45,45,45,-40,73,-38,-39,-42,45,-65,-34,-36,-41,-35,-37,]),'NOT':([27,30,31,32,33,52,],[46,46,46,46,46,46,]),'ARRAY':([27,30,31,32,33,52,],[47,47,47,47,47,47,]),'ABS':([27,30,31,32,33,52,],[48,48,48,48,48,48,]),'ENTERO':([27,30,31,32,33,44,45,46,52,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,],[49,49,49,49,49,49,49,49,49,49,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,49,]),'DECIMAL':([27,30,31,32,33,44,45,46,52,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,],[50,50,50,50,50,50,50,50,50,50,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,50,]),'CADENA':([27,30,31,32,33,44,45,46,52,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,95,],[51,51,51,51,51,51,51,51,51,51,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,51,]),'MAS':([29,38,43,49,50,51,53,54,55,61,97,98,],[-65,-40,72,-38,-39,-42,-65,-34,-36,-41,-35,-37,]),'POR':([29,38,43,49,50,51,53,54,55,61,97,98,],[-65,-40,74,-38,-39,-42,-65,-34,-36,-41,-35,-37,]),'DIVIDIDO':([29,38,43,49,50,51,53,54,55,61,97,98,],[-65,-40,75,-38,-39,-42,-65,-34,-36,-41,-35,-37,]),'RESIDUO':([29,38,43,49,50,51,53,54,55,61,97,98,],[-65,-40,76,-38,-39,-42,-65,-34,-36,-41,-35,-37,]),'AND':([29,38,43,49,50,51,53,54,55,61,97,98,],[-65,-40,77,-38,-39,-42,-65,-34,-36,-41,-35,-37,]),'OR':([29,38,43,49,50,51,53,54,55,61,97,98,],[-65,-40,78,-38,-39,-42,-65,-34,-36,-41,-35,-37,]),'XOR':([29,38,43,49,50,51,53,54,55,61,97,98,],[-65,-40,79,-38,-39,-42,-65,-34,-36,-41,-35,-37,]),'BOR':([29,38,43,49,50,51,53,54,55,61,97,98,],[-65,-40,81,-38,-39,-42,-65,-34,-36,-41,-35,-37,]),'BXOR':([29,38,43,49,50,51,53,54,55,61,97,98,],[-65,-40,82,-38,-39,-42,-65,-34,-36,-41,-35,-37,]),'SHIFTI':([29,38,43,49,50,51,53,54,55,61,97,98,],[-65,-40,83,-38,-39,-42,-65,-34,-36,-41,-35,-37,]),'SHIFTD':([29,38,43,49,50,51,53,54,55,61,97,98,],[-65,-40,84,-38,-39,-42,-65,-34,-36,-41,-35,-37,]),'IGUALQ':([29,38,43,49,50,51,53,54,55,61,97,98,],[-65,-40,85,-38,-39,-42,-65,-34,-36,-41,-35,-37,]),'NIGUALQ':([29,38,43,49,50,51,53,54,55,61,97,98,],[-65,-40,86,-38,-39,-42,-65,-34,-36,-41,-35,-37,]),'MAYORQ':([29,38,43,49,50,51,53,54,55,61,97,98,],[-65,-40,87,-38,-39,-42,-65,-34,-36,-41,-35,-37,]),'MENORQ':([29,38,43,49,50,51,53,54,55,61,97,98,],[-65,-40,88,-38,-39,-42,-65,-34,-36,-41,-35,-37,]),'MAYORIGUALQ':([29,38,43,49,50,51,53,54,55,61,97,98,],[-65,-40,89,-38,-39,-42,-65,-34,-36,-41,-35,-37,]),'MENORIGUALQ':([29,38,43,49,50,51,53,54,55,61,97,98,],[-65,-40,90,-38,-39,-42,-65,-34,-36,-41,-35,-37,]),'CORDER':([29,38,43,49,50,51,53,54,55,56,61,69,71,91,92,93,97,98,105,106,113,114,],[-65,-40,-65,-38,-39,-42,-65,-34,-36,98,-41,-25,-33,-26,-27,-28,-35,-37,-32,-29,-31,-30,]),'PARDER':([29,38,43,49,50,51,53,54,55,57,58,59,61,63,64,65,66,67,69,71,91,92,93,94,97,98,105,106,107,113,114,],[-65,-40,-65,-38,-39,-42,-65,-34,-36,99,100,101,-41,102,103,-62,-63,-64,-25,-33,-26,-27,-28,106,-35,-37,-32,-29,114,-31,-30,]),'INT':([41,],[65,]),'FLOAT':([41,],[66,]),'CHAR':([41,],[67,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([3,],[4,]),'instruccion':([3,5,22,],[5,22,22,]),'asignacion':([3,5,22,],[6,6,6,]),'array_instr':([3,5,22,],[7,7,7,]),'unset_instr':([3,5,22,],[8,8,8,]),'print_instr':([3,5,22,],[9,9,9,]),'if_instr':([3,5,22,],[10,10,10,]),'etiqueta_instr':([3,5,22,],[11,11,11,]),'goto_instr':([3,5,22,101,],[12,12,12,111,]),'exit_instr':([3,5,22,],[13,13,13,]),'instrucciones2':([5,22,],[23,37,]),'empty':([5,22,29,43,53,],[24,24,55,71,55,]),'indices':([15,38,],[28,61,]),'indice':([15,29,38,53,],[29,53,29,53,]),'exp_numerica':([27,30,31,32,33,52,],[39,56,57,58,59,96,]),'valores':([27,30,31,32,33,44,45,46,52,70,95,],[43,43,43,43,43,91,92,93,43,105,107,]),'indices2':([29,53,],[54,97,]),'tipo_dato':([41,],[64,]),'exp_numerica2':([43,],[69,]),'signo':([43,],[70,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> MAIN DOSPUNTOS instrucciones','init',3,'p_init','gramatica2.py',185),
  ('instrucciones -> instruccion instrucciones2','instrucciones',2,'p_lista_instrucciones','gramatica2.py',190),
  ('instrucciones2 -> instruccion instrucciones2','instrucciones2',2,'p_instrucciones_instruccion','gramatica2.py',198),
  ('instrucciones2 -> empty','instrucciones2',1,'p_instrucciones_instruccion2','gramatica2.py',206),
  ('instruccion -> asignacion','instruccion',1,'p_instruccion_asignacion','gramatica2.py',212),
  ('instruccion -> array_instr','instruccion',1,'p_instruccion_array','gramatica2.py',218),
  ('instruccion -> unset_instr','instruccion',1,'p_instruccion_unset','gramatica2.py',224),
  ('instruccion -> print_instr','instruccion',1,'p_instruccion_print','gramatica2.py',230),
  ('instruccion -> if_instr','instruccion',1,'p_instruccion_if','gramatica2.py',236),
  ('instruccion -> etiqueta_instr','instruccion',1,'p_instruccion_etiqueta','gramatica2.py',242),
  ('instruccion -> goto_instr','instruccion',1,'p_instruccion_goto','gramatica2.py',248),
  ('instruccion -> exit_instr','instruccion',1,'p_instruccion_exit','gramatica2.py',254),
  ('instruccion -> error PTCOMA','instruccion',2,'p_instruccion_error','gramatica2.py',260),
  ('instruccion -> error DOSPUNTOS','instruccion',2,'p_instruccion_error','gramatica2.py',261),
  ('asignacion -> VAR IGUAL exp_numerica PTCOMA','asignacion',4,'p_asignacion','gramatica2.py',264),
  ('asignacion -> VAR IGUAL READ PARIZQ PARDER PTCOMA','asignacion',6,'p_asignacion','gramatica2.py',265),
  ('asignacion -> VAR IGUAL BAND VAR PTCOMA','asignacion',5,'p_asignacion','gramatica2.py',266),
  ('array_instr -> VAR indices IGUAL exp_numerica PTCOMA','array_instr',5,'p_array','gramatica2.py',282),
  ('print_instr -> PRINT PARIZQ exp_numerica PARDER PTCOMA','print_instr',5,'p_imprimir','gramatica2.py',289),
  ('unset_instr -> UNSET PARIZQ exp_numerica PARDER PTCOMA','unset_instr',5,'p_unset','gramatica2.py',295),
  ('if_instr -> IF PARIZQ exp_numerica PARDER goto_instr','if_instr',5,'p_if','gramatica2.py',301),
  ('etiqueta_instr -> ID DOSPUNTOS','etiqueta_instr',2,'p_etiqueta','gramatica2.py',307),
  ('goto_instr -> GOTO ID PTCOMA','goto_instr',3,'p_goto','gramatica2.py',318),
  ('exit_instr -> EXIT PTCOMA','exit_instr',2,'p_exit','gramatica2.py',324),
  ('exp_numerica -> valores exp_numerica2','exp_numerica',2,'p_expresion','gramatica2.py',330),
  ('exp_numerica -> BNOT valores','exp_numerica',2,'p_expresion_unaria','gramatica2.py',418),
  ('exp_numerica -> MENOS valores','exp_numerica',2,'p_expresion_unaria','gramatica2.py',419),
  ('exp_numerica -> NOT valores','exp_numerica',2,'p_expresion_unaria','gramatica2.py',420),
  ('exp_numerica -> ARRAY PARIZQ PARDER','exp_numerica',3,'p_expresion_array','gramatica2.py',435),
  ('exp_numerica -> ABS PARIZQ valores PARDER','exp_numerica',4,'p_expresion_unaria_abs','gramatica2.py',441),
  ('exp_numerica -> PARIZQ tipo_dato PARDER VAR','exp_numerica',4,'p_expresion_conversion','gramatica2.py',447),
  ('exp_numerica2 -> signo valores','exp_numerica2',2,'p_expresion2','gramatica2.py',462),
  ('exp_numerica2 -> empty','exp_numerica2',1,'p_expresion2_2','gramatica2.py',467),
  ('indices -> indice indices2','indices',2,'p_lista_indices','gramatica2.py',472),
  ('indices2 -> indice indices2','indices2',2,'p_indices_indice','gramatica2.py',492),
  ('indices2 -> empty','indices2',1,'p_indices_indice2','gramatica2.py',512),
  ('indice -> CORIZQ exp_numerica CORDER','indice',3,'p_indice','gramatica2.py',518),
  ('valores -> ENTERO','valores',1,'p_valor_entero','gramatica2.py',524),
  ('valores -> DECIMAL','valores',1,'p_valor_decimal','gramatica2.py',530),
  ('valores -> VAR','valores',1,'p_valor_var','gramatica2.py',536),
  ('valores -> VAR indices','valores',2,'p_valor_var_indices','gramatica2.py',542),
  ('valores -> CADENA','valores',1,'p_valor_cadena','gramatica2.py',548),
  ('signo -> MAS','signo',1,'p_signo','gramatica2.py',554),
  ('signo -> MENOS','signo',1,'p_signo','gramatica2.py',555),
  ('signo -> POR','signo',1,'p_signo','gramatica2.py',556),
  ('signo -> DIVIDIDO','signo',1,'p_signo','gramatica2.py',557),
  ('signo -> RESIDUO','signo',1,'p_signo','gramatica2.py',558),
  ('signo -> AND','signo',1,'p_signo','gramatica2.py',559),
  ('signo -> OR','signo',1,'p_signo','gramatica2.py',560),
  ('signo -> XOR','signo',1,'p_signo','gramatica2.py',561),
  ('signo -> BAND','signo',1,'p_signo','gramatica2.py',562),
  ('signo -> BOR','signo',1,'p_signo','gramatica2.py',563),
  ('signo -> BXOR','signo',1,'p_signo','gramatica2.py',564),
  ('signo -> SHIFTI','signo',1,'p_signo','gramatica2.py',565),
  ('signo -> SHIFTD','signo',1,'p_signo','gramatica2.py',566),
  ('signo -> IGUALQ','signo',1,'p_signo','gramatica2.py',567),
  ('signo -> NIGUALQ','signo',1,'p_signo','gramatica2.py',568),
  ('signo -> MAYORQ','signo',1,'p_signo','gramatica2.py',569),
  ('signo -> MENORQ','signo',1,'p_signo','gramatica2.py',570),
  ('signo -> MAYORIGUALQ','signo',1,'p_signo','gramatica2.py',571),
  ('signo -> MENORIGUALQ','signo',1,'p_signo','gramatica2.py',572),
  ('tipo_dato -> INT','tipo_dato',1,'p_tipo_dato_int','gramatica2.py',576),
  ('tipo_dato -> FLOAT','tipo_dato',1,'p_tipo_dato_float','gramatica2.py',582),
  ('tipo_dato -> CHAR','tipo_dato',1,'p_tipo_dato_char','gramatica2.py',588),
  ('empty -> <empty>','empty',0,'p_empty','gramatica2.py',594),
]
