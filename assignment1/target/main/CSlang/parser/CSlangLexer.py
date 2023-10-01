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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u01d3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u0091\n\3\f\3")
        buf.write("\16\3\u0094\13\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u009c\n\4")
        buf.write("\f\4\16\4\u009f\13\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,")
        buf.write("\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\66\6\66\u015d\n\66\r\66\16")
        buf.write("\66\u015e\3\66\3\66\7\66\u0163\n\66\f\66\16\66\u0166\13")
        buf.write("\66\3\66\5\66\u0169\n\66\3\66\6\66\u016c\n\66\r\66\16")
        buf.write("\66\u016d\3\66\5\66\u0171\n\66\3\67\3\67\5\67\u0175\n")
        buf.write("\67\3\67\6\67\u0178\n\67\r\67\16\67\u0179\38\68\u017d")
        buf.write("\n8\r8\168\u017e\39\39\39\39\59\u0185\n9\3:\3:\3:\3;\3")
        buf.write(";\7;\u018c\n;\f;\16;\u018f\13;\3;\3;\3;\3<\3<\3<\3<\5")
        buf.write("<\u0198\n<\3=\3=\7=\u019c\n=\f=\16=\u019f\13=\3>\3>\3")
        buf.write(">\3>\3>\3?\3?\7?\u01a8\n?\f?\16?\u01ab\13?\3@\3@\6@\u01af")
        buf.write("\n@\r@\16@\u01b0\3A\6A\u01b4\nA\rA\16A\u01b5\3A\3A\3B")
        buf.write("\3B\7B\u01bc\nB\fB\16B\u01bf\13B\3B\3B\3C\3C\3C\3C\7C")
        buf.write("\u01c7\nC\fC\16C\u01ca\13C\3C\3C\3C\3C\3C\3D\3D\3D\3\u009d")
        buf.write("\2E\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m\2o8")
        buf.write("q\2s\2u9w\2y\2{:};\177<\u0081=\u0083>\u0085?\u0087@\3")
        buf.write("\2\16\4\2\f\f\17\17\3\2\62;\4\2GGgg\4\2--//\7\2\f\f\17")
        buf.write("\17$$))^^\t\2$$^^ddhhppttvv\3\2\63;\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\5\2\13\f\17\17\"\"\t\2))^^ddhhppttvv\6\2\f\f")
        buf.write("\17\17$$^^\2\u01e4\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2o\3\2\2")
        buf.write("\2\2u\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\3\u0089\3\2\2\2\5\u008c\3\2\2\2\7\u0097\3\2\2\2\t\u00a5")
        buf.write("\3\2\2\2\13\u00ab\3\2\2\2\r\u00b4\3\2\2\2\17\u00b7\3\2")
        buf.write("\2\2\21\u00bc\3\2\2\2\23\u00c0\3\2\2\2\25\u00c5\3\2\2")
        buf.write("\2\27\u00cb\3\2\2\2\31\u00cf\3\2\2\2\33\u00d5\3\2\2\2")
        buf.write("\35\u00da\3\2\2\2\37\u00e1\3\2\2\2!\u00e8\3\2\2\2#\u00ed")
        buf.write("\3\2\2\2%\u00f3\3\2\2\2\'\u00ff\3\2\2\2)\u0103\3\2\2\2")
        buf.write("+\u0108\3\2\2\2-\u010c\3\2\2\2/\u0111\3\2\2\2\61\u0117")
        buf.write("\3\2\2\2\63\u011c\3\2\2\2\65\u011e\3\2\2\2\67\u0120\3")
        buf.write("\2\2\29\u0122\3\2\2\2;\u0124\3\2\2\2=\u0126\3\2\2\2?\u0129")
        buf.write("\3\2\2\2A\u012b\3\2\2\2C\u012e\3\2\2\2E\u0131\3\2\2\2")
        buf.write("G\u0134\3\2\2\2I\u0137\3\2\2\2K\u0139\3\2\2\2M\u013c\3")
        buf.write("\2\2\2O\u013e\3\2\2\2Q\u0141\3\2\2\2S\u0143\3\2\2\2U\u0145")
        buf.write("\3\2\2\2W\u0147\3\2\2\2Y\u0149\3\2\2\2[\u014b\3\2\2\2")
        buf.write("]\u014d\3\2\2\2_\u014f\3\2\2\2a\u0151\3\2\2\2c\u0153\3")
        buf.write("\2\2\2e\u0155\3\2\2\2g\u0157\3\2\2\2i\u0159\3\2\2\2k\u0170")
        buf.write("\3\2\2\2m\u0172\3\2\2\2o\u017c\3\2\2\2q\u0184\3\2\2\2")
        buf.write("s\u0186\3\2\2\2u\u0189\3\2\2\2w\u0197\3\2\2\2y\u0199\3")
        buf.write("\2\2\2{\u01a0\3\2\2\2}\u01a5\3\2\2\2\177\u01ac\3\2\2\2")
        buf.write("\u0081\u01b3\3\2\2\2\u0083\u01b9\3\2\2\2\u0085\u01c2\3")
        buf.write("\2\2\2\u0087\u01d0\3\2\2\2\u0089\u008a\7>\2\2\u008a\u008b")
        buf.write("\7/\2\2\u008b\4\3\2\2\2\u008c\u008d\7\61\2\2\u008d\u008e")
        buf.write("\7\61\2\2\u008e\u0092\3\2\2\2\u008f\u0091\n\2\2\2\u0090")
        buf.write("\u008f\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2")
        buf.write("\u0092\u0093\3\2\2\2\u0093\u0095\3\2\2\2\u0094\u0092\3")
        buf.write("\2\2\2\u0095\u0096\b\3\2\2\u0096\6\3\2\2\2\u0097\u0098")
        buf.write("\7\61\2\2\u0098\u0099\7,\2\2\u0099\u009d\3\2\2\2\u009a")
        buf.write("\u009c\13\2\2\2\u009b\u009a\3\2\2\2\u009c\u009f\3\2\2")
        buf.write("\2\u009d\u009e\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u00a0")
        buf.write("\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a1\7,\2\2\u00a1")
        buf.write("\u00a2\7\61\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\b\4\2")
        buf.write("\2\u00a4\b\3\2\2\2\u00a5\u00a6\7d\2\2\u00a6\u00a7\7t\2")
        buf.write("\2\u00a7\u00a8\7g\2\2\u00a8\u00a9\7c\2\2\u00a9\u00aa\7")
        buf.write("m\2\2\u00aa\n\3\2\2\2\u00ab\u00ac\7e\2\2\u00ac\u00ad\7")
        buf.write("q\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af\7v\2\2\u00af\u00b0")
        buf.write("\7k\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2\7w\2\2\u00b2\u00b3")
        buf.write("\7g\2\2\u00b3\f\3\2\2\2\u00b4\u00b5\7k\2\2\u00b5\u00b6")
        buf.write("\7h\2\2\u00b6\16\3\2\2\2\u00b7\u00b8\7g\2\2\u00b8\u00b9")
        buf.write("\7n\2\2\u00b9\u00ba\7u\2\2\u00ba\u00bb\7g\2\2\u00bb\20")
        buf.write("\3\2\2\2\u00bc\u00bd\7h\2\2\u00bd\u00be\7q\2\2\u00be\u00bf")
        buf.write("\7t\2\2\u00bf\22\3\2\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2")
        buf.write("\7t\2\2\u00c2\u00c3\7w\2\2\u00c3\u00c4\7g\2\2\u00c4\24")
        buf.write("\3\2\2\2\u00c5\u00c6\7h\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8")
        buf.write("\7n\2\2\u00c8\u00c9\7u\2\2\u00c9\u00ca\7g\2\2\u00ca\26")
        buf.write("\3\2\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce")
        buf.write("\7v\2\2\u00ce\30\3\2\2\2\u00cf\u00d0\7h\2\2\u00d0\u00d1")
        buf.write("\7n\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3\7c\2\2\u00d3\u00d4")
        buf.write("\7v\2\2\u00d4\32\3\2\2\2\u00d5\u00d6\7d\2\2\u00d6\u00d7")
        buf.write("\7q\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7n\2\2\u00d9\34")
        buf.write("\3\2\2\2\u00da\u00db\7u\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd")
        buf.write("\7t\2\2\u00dd\u00de\7k\2\2\u00de\u00df\7p\2\2\u00df\u00e0")
        buf.write("\7i\2\2\u00e0\36\3\2\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3")
        buf.write("\7g\2\2\u00e3\u00e4\7v\2\2\u00e4\u00e5\7w\2\2\u00e5\u00e6")
        buf.write("\7t\2\2\u00e6\u00e7\7p\2\2\u00e7 \3\2\2\2\u00e8\u00e9")
        buf.write("\7p\2\2\u00e9\u00ea\7w\2\2\u00ea\u00eb\7n\2\2\u00eb\u00ec")
        buf.write("\7n\2\2\u00ec\"\3\2\2\2\u00ed\u00ee\7e\2\2\u00ee\u00ef")
        buf.write("\7n\2\2\u00ef\u00f0\7c\2\2\u00f0\u00f1\7u\2\2\u00f1\u00f2")
        buf.write("\7u\2\2\u00f2$\3\2\2\2\u00f3\u00f4\7e\2\2\u00f4\u00f5")
        buf.write("\7q\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7\7u\2\2\u00f7\u00f8")
        buf.write("\7v\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa\7w\2\2\u00fa\u00fb")
        buf.write("\7e\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe")
        buf.write("\7t\2\2\u00fe&\3\2\2\2\u00ff\u0100\7x\2\2\u0100\u0101")
        buf.write("\7c\2\2\u0101\u0102\7t\2\2\u0102(\3\2\2\2\u0103\u0104")
        buf.write("\7u\2\2\u0104\u0105\7g\2\2\u0105\u0106\7n\2\2\u0106\u0107")
        buf.write("\7h\2\2\u0107*\3\2\2\2\u0108\u0109\7p\2\2\u0109\u010a")
        buf.write("\7g\2\2\u010a\u010b\7y\2\2\u010b,\3\2\2\2\u010c\u010d")
        buf.write("\7x\2\2\u010d\u010e\7q\2\2\u010e\u010f\7k\2\2\u010f\u0110")
        buf.write("\7f\2\2\u0110.\3\2\2\2\u0111\u0112\7e\2\2\u0112\u0113")
        buf.write("\7q\2\2\u0113\u0114\7p\2\2\u0114\u0115\7u\2\2\u0115\u0116")
        buf.write("\7v\2\2\u0116\60\3\2\2\2\u0117\u0118\7h\2\2\u0118\u0119")
        buf.write("\7w\2\2\u0119\u011a\7p\2\2\u011a\u011b\7e\2\2\u011b\62")
        buf.write("\3\2\2\2\u011c\u011d\7-\2\2\u011d\64\3\2\2\2\u011e\u011f")
        buf.write("\7/\2\2\u011f\66\3\2\2\2\u0120\u0121\7,\2\2\u01218\3\2")
        buf.write("\2\2\u0122\u0123\7\61\2\2\u0123:\3\2\2\2\u0124\u0125\7")
        buf.write("^\2\2\u0125<\3\2\2\2\u0126\u0127\7#\2\2\u0127\u0128\7")
        buf.write("?\2\2\u0128>\3\2\2\2\u0129\u012a\7#\2\2\u012a@\3\2\2\2")
        buf.write("\u012b\u012c\7(\2\2\u012c\u012d\7(\2\2\u012dB\3\2\2\2")
        buf.write("\u012e\u012f\7~\2\2\u012f\u0130\7~\2\2\u0130D\3\2\2\2")
        buf.write("\u0131\u0132\7?\2\2\u0132\u0133\7?\2\2\u0133F\3\2\2\2")
        buf.write("\u0134\u0135\7<\2\2\u0135\u0136\7?\2\2\u0136H\3\2\2\2")
        buf.write("\u0137\u0138\7?\2\2\u0138J\3\2\2\2\u0139\u013a\7>\2\2")
        buf.write("\u013a\u013b\7?\2\2\u013bL\3\2\2\2\u013c\u013d\7>\2\2")
        buf.write("\u013dN\3\2\2\2\u013e\u013f\7@\2\2\u013f\u0140\7?\2\2")
        buf.write("\u0140P\3\2\2\2\u0141\u0142\7@\2\2\u0142R\3\2\2\2\u0143")
        buf.write("\u0144\7`\2\2\u0144T\3\2\2\2\u0145\u0146\7\'\2\2\u0146")
        buf.write("V\3\2\2\2\u0147\u0148\7*\2\2\u0148X\3\2\2\2\u0149\u014a")
        buf.write("\7+\2\2\u014aZ\3\2\2\2\u014b\u014c\7]\2\2\u014c\\\3\2")
        buf.write("\2\2\u014d\u014e\7_\2\2\u014e^\3\2\2\2\u014f\u0150\7\60")
        buf.write("\2\2\u0150`\3\2\2\2\u0151\u0152\7.\2\2\u0152b\3\2\2\2")
        buf.write("\u0153\u0154\7}\2\2\u0154d\3\2\2\2\u0155\u0156\7\177\2")
        buf.write("\2\u0156f\3\2\2\2\u0157\u0158\7=\2\2\u0158h\3\2\2\2\u0159")
        buf.write("\u015a\7<\2\2\u015aj\3\2\2\2\u015b\u015d\t\3\2\2\u015c")
        buf.write("\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015c\3\2\2\2")
        buf.write("\u015e\u015f\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0164\7")
        buf.write("\60\2\2\u0161\u0163\t\3\2\2\u0162\u0161\3\2\2\2\u0163")
        buf.write("\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2")
        buf.write("\u0165\u0168\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u0169\5")
        buf.write("m\67\2\u0168\u0167\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u0171")
        buf.write("\3\2\2\2\u016a\u016c\t\3\2\2\u016b\u016a\3\2\2\2\u016c")
        buf.write("\u016d\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2")
        buf.write("\u016e\u016f\3\2\2\2\u016f\u0171\5m\67\2\u0170\u015c\3")
        buf.write("\2\2\2\u0170\u016b\3\2\2\2\u0171l\3\2\2\2\u0172\u0174")
        buf.write("\t\4\2\2\u0173\u0175\t\5\2\2\u0174\u0173\3\2\2\2\u0174")
        buf.write("\u0175\3\2\2\2\u0175\u0177\3\2\2\2\u0176\u0178\t\3\2\2")
        buf.write("\u0177\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u0177\3")
        buf.write("\2\2\2\u0179\u017a\3\2\2\2\u017an\3\2\2\2\u017b\u017d")
        buf.write("\t\3\2\2\u017c\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e")
        buf.write("\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017fp\3\2\2\2\u0180")
        buf.write("\u0185\n\6\2\2\u0181\u0185\5s:\2\u0182\u0183\7)\2\2\u0183")
        buf.write("\u0185\7$\2\2\u0184\u0180\3\2\2\2\u0184\u0181\3\2\2\2")
        buf.write("\u0184\u0182\3\2\2\2\u0185r\3\2\2\2\u0186\u0187\7^\2\2")
        buf.write("\u0187\u0188\t\7\2\2\u0188t\3\2\2\2\u0189\u018d\7$\2\2")
        buf.write("\u018a\u018c\5q9\2\u018b\u018a\3\2\2\2\u018c\u018f\3\2")
        buf.write("\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u0190")
        buf.write("\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0191\7$\2\2\u0191")
        buf.write("\u0192\b;\3\2\u0192v\3\2\2\2\u0193\u0198\5\33\16\2\u0194")
        buf.write("\u0198\5\27\f\2\u0195\u0198\5\31\r\2\u0196\u0198\5\35")
        buf.write("\17\2\u0197\u0193\3\2\2\2\u0197\u0194\3\2\2\2\u0197\u0195")
        buf.write("\3\2\2\2\u0197\u0196\3\2\2\2\u0198x\3\2\2\2\u0199\u019d")
        buf.write("\t\b\2\2\u019a\u019c\t\3\2\2\u019b\u019a\3\2\2\2\u019c")
        buf.write("\u019f\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019e\3\2\2\2")
        buf.write("\u019ez\3\2\2\2\u019f\u019d\3\2\2\2\u01a0\u01a1\5[.\2")
        buf.write("\u01a1\u01a2\5y=\2\u01a2\u01a3\5]/\2\u01a3\u01a4\5w<\2")
        buf.write("\u01a4|\3\2\2\2\u01a5\u01a9\t\t\2\2\u01a6\u01a8\t\n\2")
        buf.write("\2\u01a7\u01a6\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7")
        buf.write("\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa~\3\2\2\2\u01ab\u01a9")
        buf.write("\3\2\2\2\u01ac\u01ae\7B\2\2\u01ad\u01af\t\n\2\2\u01ae")
        buf.write("\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01ae\3\2\2\2")
        buf.write("\u01b0\u01b1\3\2\2\2\u01b1\u0080\3\2\2\2\u01b2\u01b4\t")
        buf.write("\13\2\2\u01b3\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5")
        buf.write("\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b7\3\2\2\2")
        buf.write("\u01b7\u01b8\bA\2\2\u01b8\u0082\3\2\2\2\u01b9\u01bd\7")
        buf.write("$\2\2\u01ba\u01bc\5q9\2\u01bb\u01ba\3\2\2\2\u01bc\u01bf")
        buf.write("\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be")
        buf.write("\u01c0\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0\u01c1\bB\4\2")
        buf.write("\u01c1\u0084\3\2\2\2\u01c2\u01c8\7$\2\2\u01c3\u01c4\7")
        buf.write("^\2\2\u01c4\u01c7\t\f\2\2\u01c5\u01c7\n\r\2\2\u01c6\u01c3")
        buf.write("\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8")
        buf.write("\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01cb\3\2\2\2")
        buf.write("\u01ca\u01c8\3\2\2\2\u01cb\u01cc\7^\2\2\u01cc\u01cd\n")
        buf.write("\f\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cf\bC\5\2\u01cf\u0086")
        buf.write("\3\2\2\2\u01d0\u01d1\13\2\2\2\u01d1\u01d2\bD\6\2\u01d2")
        buf.write("\u0088\3\2\2\2\27\2\u0092\u009d\u015e\u0164\u0168\u016d")
        buf.write("\u0170\u0174\u0179\u017e\u0184\u018d\u0197\u019d\u01a9")
        buf.write("\u01b0\u01b5\u01bd\u01c6\u01c8\7\b\2\2\3;\2\3B\3\3C\4")
        buf.write("\3D\5")
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
    NOT_EQUAL = 30
    NEGATE = 31
    AND = 32
    OR = 33
    EQUAL = 34
    DECLARE_ASSIGN_OP = 35
    ASSIGN_OP = 36
    LESS_EQUAL = 37
    LESS_THAN = 38
    GREATER_EQUAL = 39
    GREATER_THAN = 40
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
    FLOAT_LIT = 53
    INT_LIT = 54
    STRING_LIT = 55
    ARRAY_TYPE = 56
    ID = 57
    AT_ID = 58
    WS = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61
    ERROR_CHAR = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<-'", "'break'", "'continue'", "'if'", "'else'", "'for'", 
            "'true'", "'false'", "'int'", "'float'", "'bool'", "'string'", 
            "'return'", "'null'", "'class'", "'constructor'", "'var'", "'self'", 
            "'new'", "'void'", "'const'", "'func'", "'+'", "'-'", "'*'", 
            "'/'", "'\\'", "'!='", "'!'", "'&&'", "'||'", "'=='", "':='", 
            "'='", "'<='", "'<'", "'>='", "'>'", "'^'", "'%'", "'('", "')'", 
            "'['", "']'", "'.'", "','", "'{'", "'}'", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "LINE_COMMENT", "BLOCK_COMMENT", "BREAK", "CONTINUE", "IF", 
            "ELSE", "FOR", "TRUE", "FALSE", "INT", "FLOAT", "BOOL", "STRING", 
            "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", 
            "VOID", "CONST", "FUNC", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", 
            "BACKSLASH", "NOT_EQUAL", "NEGATE", "AND", "OR", "EQUAL", "DECLARE_ASSIGN_OP", 
            "ASSIGN_OP", "LESS_EQUAL", "LESS_THAN", "GREATER_EQUAL", "GREATER_THAN", 
            "POW_OP", "MOD_OP", "LB", "RB", "LS", "RS", "DOT", "CM", "LP", 
            "RP", "SEMI", "COLON", "FLOAT_LIT", "INT_LIT", "STRING_LIT", 
            "ARRAY_TYPE", "ID", "AT_ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "LINE_COMMENT", "BLOCK_COMMENT", "BREAK", "CONTINUE", 
                  "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", "FLOAT", 
                  "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
                  "VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", "ADD_OP", 
                  "SUB_OP", "MUL_OP", "DIV_OP", "BACKSLASH", "NOT_EQUAL", 
                  "NEGATE", "AND", "OR", "EQUAL", "DECLARE_ASSIGN_OP", "ASSIGN_OP", 
                  "LESS_EQUAL", "LESS_THAN", "GREATER_EQUAL", "GREATER_THAN", 
                  "POW_OP", "MOD_OP", "LB", "RB", "LS", "RS", "DOT", "CM", 
                  "LP", "RP", "SEMI", "COLON", "FLOAT_LIT", "EXPONENT", 
                  "INT_LIT", "CHAR_LIT", "ESC", "STRING_LIT", "ELEMENT_TYPE", 
                  "INT_LIT_NON_ZERO", "ARRAY_TYPE", "ID", "AT_ID", "WS", 
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
            actions[57] = self.STRING_LIT_action 
            actions[64] = self.UNCLOSE_STRING_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            actions[66] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


