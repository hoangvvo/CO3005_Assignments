# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u01ca\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u0093\n")
        buf.write("\3\f\3\16\3\u0096\13\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u009e")
        buf.write("\n\4\f\4\16\4\u00a1\13\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3,")
        buf.write("\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\66\3\66")
        buf.write("\5\66\u0163\n\66\3\67\3\67\3\67\3\67\5\67\u0169\n\67\3")
        buf.write("8\68\u016c\n8\r8\168\u016d\38\38\78\u0172\n8\f8\168\u0175")
        buf.write("\138\38\58\u0178\n8\38\68\u017b\n8\r8\168\u017c\38\58")
        buf.write("\u0180\n8\39\39\59\u0184\n9\39\69\u0187\n9\r9\169\u0188")
        buf.write("\3:\6:\u018c\n:\r:\16:\u018d\3;\3;\5;\u0192\n;\3<\3<\3")
        buf.write("<\7<\u0197\n<\f<\16<\u019a\13<\3<\3<\3=\3=\3=\3>\3>\5")
        buf.write(">\u01a3\n>\3>\3>\3>\7>\u01a8\n>\f>\16>\u01ab\13>\3>\3")
        buf.write(">\3?\3?\7?\u01b1\n?\f?\16?\u01b4\13?\3@\3@\3@\3A\3A\5")
        buf.write("A\u01bb\nA\3B\6B\u01be\nB\rB\16B\u01bf\3B\3B\3C\3C\3D")
        buf.write("\3D\3E\3E\3E\3\u009f\2F\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q\2s:u;w<y\2{=}>\177?\u0081@\u0083")
        buf.write("A\u0085B\u0087C\u0089D\3\2\13\4\2\f\f\17\17\3\2\62;\4")
        buf.write("\2GGgg\4\2--//\5\2\f\f\17\17$$\t\2$$^^ddhhppttvv\5\2C")
        buf.write("\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2\u01e0\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\3\u008b\3\2\2\2\5\u008e")
        buf.write("\3\2\2\2\7\u0099\3\2\2\2\t\u00a7\3\2\2\2\13\u00ad\3\2")
        buf.write("\2\2\r\u00b6\3\2\2\2\17\u00b9\3\2\2\2\21\u00be\3\2\2\2")
        buf.write("\23\u00c2\3\2\2\2\25\u00c7\3\2\2\2\27\u00cd\3\2\2\2\31")
        buf.write("\u00d1\3\2\2\2\33\u00d7\3\2\2\2\35\u00dc\3\2\2\2\37\u00e3")
        buf.write("\3\2\2\2!\u00ea\3\2\2\2#\u00ef\3\2\2\2%\u00f5\3\2\2\2")
        buf.write("\'\u0101\3\2\2\2)\u0105\3\2\2\2+\u010a\3\2\2\2-\u010e")
        buf.write("\3\2\2\2/\u0113\3\2\2\2\61\u0119\3\2\2\2\63\u011e\3\2")
        buf.write("\2\2\65\u0120\3\2\2\2\67\u0122\3\2\2\29\u0124\3\2\2\2")
        buf.write(";\u0126\3\2\2\2=\u0128\3\2\2\2?\u012a\3\2\2\2A\u012d\3")
        buf.write("\2\2\2C\u0130\3\2\2\2E\u0133\3\2\2\2G\u0135\3\2\2\2I\u0138")
        buf.write("\3\2\2\2K\u013a\3\2\2\2M\u013d\3\2\2\2O\u013f\3\2\2\2")
        buf.write("Q\u0142\3\2\2\2S\u0145\3\2\2\2U\u0147\3\2\2\2W\u0149\3")
        buf.write("\2\2\2Y\u014b\3\2\2\2[\u014d\3\2\2\2]\u014f\3\2\2\2_\u0151")
        buf.write("\3\2\2\2a\u0153\3\2\2\2c\u0155\3\2\2\2e\u0157\3\2\2\2")
        buf.write("g\u0159\3\2\2\2i\u015b\3\2\2\2k\u0162\3\2\2\2m\u0168\3")
        buf.write("\2\2\2o\u017f\3\2\2\2q\u0181\3\2\2\2s\u018b\3\2\2\2u\u0191")
        buf.write("\3\2\2\2w\u0193\3\2\2\2y\u019d\3\2\2\2{\u01a0\3\2\2\2")
        buf.write("}\u01ae\3\2\2\2\177\u01b5\3\2\2\2\u0081\u01ba\3\2\2\2")
        buf.write("\u0083\u01bd\3\2\2\2\u0085\u01c3\3\2\2\2\u0087\u01c5\3")
        buf.write("\2\2\2\u0089\u01c7\3\2\2\2\u008b\u008c\7>\2\2\u008c\u008d")
        buf.write("\7/\2\2\u008d\4\3\2\2\2\u008e\u008f\7\61\2\2\u008f\u0090")
        buf.write("\7\61\2\2\u0090\u0094\3\2\2\2\u0091\u0093\n\2\2\2\u0092")
        buf.write("\u0091\3\2\2\2\u0093\u0096\3\2\2\2\u0094\u0092\3\2\2\2")
        buf.write("\u0094\u0095\3\2\2\2\u0095\u0097\3\2\2\2\u0096\u0094\3")
        buf.write("\2\2\2\u0097\u0098\b\3\2\2\u0098\6\3\2\2\2\u0099\u009a")
        buf.write("\7\61\2\2\u009a\u009b\7,\2\2\u009b\u009f\3\2\2\2\u009c")
        buf.write("\u009e\13\2\2\2\u009d\u009c\3\2\2\2\u009e\u00a1\3\2\2")
        buf.write("\2\u009f\u00a0\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a2")
        buf.write("\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a3\7,\2\2\u00a3")
        buf.write("\u00a4\7\61\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\b\4\2")
        buf.write("\2\u00a6\b\3\2\2\2\u00a7\u00a8\7d\2\2\u00a8\u00a9\7t\2")
        buf.write("\2\u00a9\u00aa\7g\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac\7")
        buf.write("m\2\2\u00ac\n\3\2\2\2\u00ad\u00ae\7e\2\2\u00ae\u00af\7")
        buf.write("q\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b2")
        buf.write("\7k\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5")
        buf.write("\7g\2\2\u00b5\f\3\2\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8")
        buf.write("\7h\2\2\u00b8\16\3\2\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb")
        buf.write("\7n\2\2\u00bb\u00bc\7u\2\2\u00bc\u00bd\7g\2\2\u00bd\20")
        buf.write("\3\2\2\2\u00be\u00bf\7h\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1")
        buf.write("\7t\2\2\u00c1\22\3\2\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4")
        buf.write("\7t\2\2\u00c4\u00c5\7w\2\2\u00c5\u00c6\7g\2\2\u00c6\24")
        buf.write("\3\2\2\2\u00c7\u00c8\7h\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca")
        buf.write("\7n\2\2\u00ca\u00cb\7u\2\2\u00cb\u00cc\7g\2\2\u00cc\26")
        buf.write("\3\2\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7p\2\2\u00cf\u00d0")
        buf.write("\7v\2\2\u00d0\30\3\2\2\2\u00d1\u00d2\7h\2\2\u00d2\u00d3")
        buf.write("\7n\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6")
        buf.write("\7v\2\2\u00d6\32\3\2\2\2\u00d7\u00d8\7d\2\2\u00d8\u00d9")
        buf.write("\7q\2\2\u00d9\u00da\7q\2\2\u00da\u00db\7n\2\2\u00db\34")
        buf.write("\3\2\2\2\u00dc\u00dd\7u\2\2\u00dd\u00de\7v\2\2\u00de\u00df")
        buf.write("\7t\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2")
        buf.write("\7i\2\2\u00e2\36\3\2\2\2\u00e3\u00e4\7t\2\2\u00e4\u00e5")
        buf.write("\7g\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7\7w\2\2\u00e7\u00e8")
        buf.write("\7t\2\2\u00e8\u00e9\7p\2\2\u00e9 \3\2\2\2\u00ea\u00eb")
        buf.write("\7p\2\2\u00eb\u00ec\7w\2\2\u00ec\u00ed\7n\2\2\u00ed\u00ee")
        buf.write("\7n\2\2\u00ee\"\3\2\2\2\u00ef\u00f0\7e\2\2\u00f0\u00f1")
        buf.write("\7n\2\2\u00f1\u00f2\7c\2\2\u00f2\u00f3\7u\2\2\u00f3\u00f4")
        buf.write("\7u\2\2\u00f4$\3\2\2\2\u00f5\u00f6\7e\2\2\u00f6\u00f7")
        buf.write("\7q\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9\7u\2\2\u00f9\u00fa")
        buf.write("\7v\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc\7w\2\2\u00fc\u00fd")
        buf.write("\7e\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7q\2\2\u00ff\u0100")
        buf.write("\7t\2\2\u0100&\3\2\2\2\u0101\u0102\7x\2\2\u0102\u0103")
        buf.write("\7c\2\2\u0103\u0104\7t\2\2\u0104(\3\2\2\2\u0105\u0106")
        buf.write("\7u\2\2\u0106\u0107\7g\2\2\u0107\u0108\7n\2\2\u0108\u0109")
        buf.write("\7h\2\2\u0109*\3\2\2\2\u010a\u010b\7p\2\2\u010b\u010c")
        buf.write("\7g\2\2\u010c\u010d\7y\2\2\u010d,\3\2\2\2\u010e\u010f")
        buf.write("\7x\2\2\u010f\u0110\7q\2\2\u0110\u0111\7k\2\2\u0111\u0112")
        buf.write("\7f\2\2\u0112.\3\2\2\2\u0113\u0114\7e\2\2\u0114\u0115")
        buf.write("\7q\2\2\u0115\u0116\7p\2\2\u0116\u0117\7u\2\2\u0117\u0118")
        buf.write("\7v\2\2\u0118\60\3\2\2\2\u0119\u011a\7h\2\2\u011a\u011b")
        buf.write("\7w\2\2\u011b\u011c\7p\2\2\u011c\u011d\7e\2\2\u011d\62")
        buf.write("\3\2\2\2\u011e\u011f\7-\2\2\u011f\64\3\2\2\2\u0120\u0121")
        buf.write("\7/\2\2\u0121\66\3\2\2\2\u0122\u0123\7,\2\2\u01238\3\2")
        buf.write("\2\2\u0124\u0125\7\61\2\2\u0125:\3\2\2\2\u0126\u0127\7")
        buf.write("^\2\2\u0127<\3\2\2\2\u0128\u0129\7#\2\2\u0129>\3\2\2\2")
        buf.write("\u012a\u012b\7(\2\2\u012b\u012c\7(\2\2\u012c@\3\2\2\2")
        buf.write("\u012d\u012e\7~\2\2\u012e\u012f\7~\2\2\u012fB\3\2\2\2")
        buf.write("\u0130\u0131\7?\2\2\u0131\u0132\7?\2\2\u0132D\3\2\2\2")
        buf.write("\u0133\u0134\7?\2\2\u0134F\3\2\2\2\u0135\u0136\7#\2\2")
        buf.write("\u0136\u0137\7?\2\2\u0137H\3\2\2\2\u0138\u0139\7>\2\2")
        buf.write("\u0139J\3\2\2\2\u013a\u013b\7>\2\2\u013b\u013c\7?\2\2")
        buf.write("\u013cL\3\2\2\2\u013d\u013e\7@\2\2\u013eN\3\2\2\2\u013f")
        buf.write("\u0140\7@\2\2\u0140\u0141\7?\2\2\u0141P\3\2\2\2\u0142")
        buf.write("\u0143\7<\2\2\u0143\u0144\7?\2\2\u0144R\3\2\2\2\u0145")
        buf.write("\u0146\7`\2\2\u0146T\3\2\2\2\u0147\u0148\7\'\2\2\u0148")
        buf.write("V\3\2\2\2\u0149\u014a\7*\2\2\u014aX\3\2\2\2\u014b\u014c")
        buf.write("\7+\2\2\u014cZ\3\2\2\2\u014d\u014e\7]\2\2\u014e\\\3\2")
        buf.write("\2\2\u014f\u0150\7_\2\2\u0150^\3\2\2\2\u0151\u0152\7\60")
        buf.write("\2\2\u0152`\3\2\2\2\u0153\u0154\7.\2\2\u0154b\3\2\2\2")
        buf.write("\u0155\u0156\7}\2\2\u0156d\3\2\2\2\u0157\u0158\7\177\2")
        buf.write("\2\u0158f\3\2\2\2\u0159\u015a\7=\2\2\u015ah\3\2\2\2\u015b")
        buf.write("\u015c\7<\2\2\u015cj\3\2\2\2\u015d\u0163\5s:\2\u015e\u0163")
        buf.write("\5o8\2\u015f\u0163\5u;\2\u0160\u0163\5w<\2\u0161\u0163")
        buf.write("\5{>\2\u0162\u015d\3\2\2\2\u0162\u015e\3\2\2\2\u0162\u015f")
        buf.write("\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0161\3\2\2\2\u0163")
        buf.write("l\3\2\2\2\u0164\u0169\5s:\2\u0165\u0169\5o8\2\u0166\u0169")
        buf.write("\5u;\2\u0167\u0169\5w<\2\u0168\u0164\3\2\2\2\u0168\u0165")
        buf.write("\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0167\3\2\2\2\u0169")
        buf.write("n\3\2\2\2\u016a\u016c\t\3\2\2\u016b\u016a\3\2\2\2\u016c")
        buf.write("\u016d\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2")
        buf.write("\u016e\u016f\3\2\2\2\u016f\u0173\7\60\2\2\u0170\u0172")
        buf.write("\t\3\2\2\u0171\u0170\3\2\2\2\u0172\u0175\3\2\2\2\u0173")
        buf.write("\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0177\3\2\2\2")
        buf.write("\u0175\u0173\3\2\2\2\u0176\u0178\5q9\2\u0177\u0176\3\2")
        buf.write("\2\2\u0177\u0178\3\2\2\2\u0178\u0180\3\2\2\2\u0179\u017b")
        buf.write("\t\3\2\2\u017a\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c")
        buf.write("\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017e\3\2\2\2")
        buf.write("\u017e\u0180\5q9\2\u017f\u016b\3\2\2\2\u017f\u017a\3\2")
        buf.write("\2\2\u0180p\3\2\2\2\u0181\u0183\t\4\2\2\u0182\u0184\t")
        buf.write("\5\2\2\u0183\u0182\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0186")
        buf.write("\3\2\2\2\u0185\u0187\t\3\2\2\u0186\u0185\3\2\2\2\u0187")
        buf.write("\u0188\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2")
        buf.write("\u0189r\3\2\2\2\u018a\u018c\t\3\2\2\u018b\u018a\3\2\2")
        buf.write("\2\u018c\u018d\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e")
        buf.write("\3\2\2\2\u018et\3\2\2\2\u018f\u0192\5\23\n\2\u0190\u0192")
        buf.write("\5\25\13\2\u0191\u018f\3\2\2\2\u0191\u0190\3\2\2\2\u0192")
        buf.write("v\3\2\2\2\u0193\u0198\7$\2\2\u0194\u0197\5y=\2\u0195\u0197")
        buf.write("\n\6\2\2\u0196\u0194\3\2\2\2\u0196\u0195\3\2\2\2\u0197")
        buf.write("\u019a\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0199\u019b\3\2\2\2\u019a\u0198\3\2\2\2\u019b\u019c\7")
        buf.write("$\2\2\u019cx\3\2\2\2\u019d\u019e\7^\2\2\u019e\u019f\t")
        buf.write("\7\2\2\u019fz\3\2\2\2\u01a0\u01a2\5[.\2\u01a1\u01a3\5")
        buf.write("m\67\2\u01a2\u01a1\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a9")
        buf.write("\3\2\2\2\u01a4\u01a5\5a\61\2\u01a5\u01a6\5m\67\2\u01a6")
        buf.write("\u01a8\3\2\2\2\u01a7\u01a4\3\2\2\2\u01a8\u01ab\3\2\2\2")
        buf.write("\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ac\3")
        buf.write("\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ad\5]/\2\u01ad|\3")
        buf.write("\2\2\2\u01ae\u01b2\t\b\2\2\u01af\u01b1\t\t\2\2\u01b0\u01af")
        buf.write("\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3~\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5")
        buf.write("\u01b6\7B\2\2\u01b6\u01b7\5}?\2\u01b7\u0080\3\2\2\2\u01b8")
        buf.write("\u01bb\5}?\2\u01b9\u01bb\5\177@\2\u01ba\u01b8\3\2\2\2")
        buf.write("\u01ba\u01b9\3\2\2\2\u01bb\u0082\3\2\2\2\u01bc\u01be\t")
        buf.write("\n\2\2\u01bd\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01bd")
        buf.write("\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1")
        buf.write("\u01c2\bB\2\2\u01c2\u0084\3\2\2\2\u01c3\u01c4\13\2\2\2")
        buf.write("\u01c4\u0086\3\2\2\2\u01c5\u01c6\13\2\2\2\u01c6\u0088")
        buf.write("\3\2\2\2\u01c7\u01c8\13\2\2\2\u01c8\u01c9\bE\3\2\u01c9")
        buf.write("\u008a\3\2\2\2\27\2\u0094\u009f\u0162\u0168\u016d\u0173")
        buf.write("\u0177\u017c\u017f\u0183\u0188\u018d\u0191\u0196\u0198")
        buf.write("\u01a2\u01a9\u01b2\u01ba\u01bf\4\b\2\2\3E\2")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    LINE_COMMENT = 2
    BLOCK_COMMENT = 3
    BREAK = 4
    CONTINUE = 5
    IF = 6
    ELSE = 7
    FOR = 8
    TRUE = 9
    FALSE = 10
    INT = 11
    FLOAT = 12
    BOOL = 13
    STRING = 14
    RETURN = 15
    NULL = 16
    CLASS = 17
    CONSTRUCTOR = 18
    VAR = 19
    SELF = 20
    NEW = 21
    VOID = 22
    CONST = 23
    FUNC = 24
    ADD_OP = 25
    SUB_OP = 26
    MUL_OP = 27
    DIV_OP = 28
    BACKSLASH = 29
    NEGATE = 30
    AND = 31
    OR = 32
    EQUAL = 33
    ASSIGN_OP = 34
    NOT_EQUAL = 35
    LESS_THAN = 36
    LESS_EQUAL = 37
    GREATER_THAN = 38
    GREATER_EQUAL = 39
    DECLARE_ASSIGN_OP = 40
    POW_OP = 41
    MOD_OP = 42
    LB = 43
    RB = 44
    LS = 45
    RS = 46
    DOT = 47
    CM = 48
    LP = 49
    RP = 50
    SEMI = 51
    COLON = 52
    LIT = 53
    LIT_EXCEPT_ARRAY = 54
    FLOAT_LIT = 55
    INT_LIT = 56
    BOOL_LIT = 57
    STRING_LIT = 58
    ARRAY_LIT = 59
    ID = 60
    AT_ID = 61
    MEMBER_ID = 62
    WS = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65
    ERROR_CHAR = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<-'", "'break'", "'continue'", "'if'", "'else'", "'for'", 
            "'true'", "'false'", "'int'", "'float'", "'bool'", "'string'", 
            "'return'", "'null'", "'class'", "'constructor'", "'var'", "'self'", 
            "'new'", "'void'", "'const'", "'func'", "'+'", "'-'", "'*'", 
            "'/'", "'\\'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "':='", "'^'", "'%'", "'('", "')'", 
            "'['", "']'", "'.'", "','", "'{'", "'}'", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "LINE_COMMENT", "BLOCK_COMMENT", "BREAK", "CONTINUE", "IF", 
            "ELSE", "FOR", "TRUE", "FALSE", "INT", "FLOAT", "BOOL", "STRING", 
            "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", 
            "VOID", "CONST", "FUNC", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", 
            "BACKSLASH", "NEGATE", "AND", "OR", "EQUAL", "ASSIGN_OP", "NOT_EQUAL", 
            "LESS_THAN", "LESS_EQUAL", "GREATER_THAN", "GREATER_EQUAL", 
            "DECLARE_ASSIGN_OP", "POW_OP", "MOD_OP", "LB", "RB", "LS", "RS", 
            "DOT", "CM", "LP", "RP", "SEMI", "COLON", "LIT", "LIT_EXCEPT_ARRAY", 
            "FLOAT_LIT", "INT_LIT", "BOOL_LIT", "STRING_LIT", "ARRAY_LIT", 
            "ID", "AT_ID", "MEMBER_ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "LINE_COMMENT", "BLOCK_COMMENT", "BREAK", "CONTINUE", 
                  "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", "FLOAT", 
                  "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
                  "VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", "ADD_OP", 
                  "SUB_OP", "MUL_OP", "DIV_OP", "BACKSLASH", "NEGATE", "AND", 
                  "OR", "EQUAL", "ASSIGN_OP", "NOT_EQUAL", "LESS_THAN", 
                  "LESS_EQUAL", "GREATER_THAN", "GREATER_EQUAL", "DECLARE_ASSIGN_OP", 
                  "POW_OP", "MOD_OP", "LB", "RB", "LS", "RS", "DOT", "CM", 
                  "LP", "RP", "SEMI", "COLON", "LIT", "LIT_EXCEPT_ARRAY", 
                  "FLOAT_LIT", "EXPONENT", "INT_LIT", "BOOL_LIT", "STRING_LIT", 
                  "ESC", "ARRAY_LIT", "ID", "AT_ID", "MEMBER_ID", "WS", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "CSlang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[67] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


