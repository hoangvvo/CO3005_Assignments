# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u01c0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\3\2\6")
        buf.write("\2L\n\2\r\2\16\2M\3\2\3\2\3\3\3\3\5\3T\n\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\5\7\5_\n\5\f\5\16\5b\13\5\3\6\3")
        buf.write("\6\5\6f\n\6\3\7\3\7\3\7\3\7\7\7l\n\7\f\7\16\7o\13\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\7\7w\n\7\f\7\16\7z\13\7\5\7|\n")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\5\b\u0084\n\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\5\t\u008d\n\t\3\t\3\t\3\t\3\t\5\t\u0093")
        buf.write("\n\t\3\t\3\t\3\n\3\n\3\n\7\n\u009a\n\n\f\n\16\n\u009d")
        buf.write("\13\n\3\13\3\13\3\13\7\13\u00a2\n\13\f\13\16\13\u00a5")
        buf.write("\13\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\5\f\u00af\n")
        buf.write("\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u00b9\n")
        buf.write("\16\f\16\16\16\u00bc\13\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\7\17\u00c4\n\17\f\17\16\17\u00c7\13\17\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\7\20\u00cf\n\20\f\20\16\20\u00d2\13")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u00da\n\21\f\21")
        buf.write("\16\21\u00dd\13\21\3\22\3\22\3\22\3\22\3\22\3\22\7\22")
        buf.write("\u00e5\n\22\f\22\16\22\u00e8\13\22\3\23\3\23\3\23\5\23")
        buf.write("\u00ed\n\23\3\24\3\24\3\24\5\24\u00f2\n\24\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\7\25\u00fc\n\25\f\25\16\25")
        buf.write("\u00ff\13\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\7\26\u010b\n\26\f\26\16\26\u010e\13\26\3\26\3")
        buf.write("\26\5\26\u0112\n\26\7\26\u0114\n\26\f\26\16\26\u0117\13")
        buf.write("\26\3\27\3\27\5\27\u011b\n\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\7\27\u0122\n\27\f\27\16\27\u0125\13\27\3\27\3\27\5\27")
        buf.write("\u0129\n\27\3\27\5\27\u012c\n\27\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\7\30\u0134\n\30\f\30\16\30\u0137\13\30\5\30\u0139")
        buf.write("\n\30\3\30\3\30\5\30\u013d\n\30\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\5\31\u0146\n\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\5\32\u0151\n\32\3\33\3\33\3\33\3")
        buf.write("\33\7\33\u0157\n\33\f\33\16\33\u015a\13\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\7\33\u0162\n\33\f\33\16\33\u0165\13")
        buf.write("\33\5\33\u0167\n\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\5\35\u0172\n\35\3\35\3\35\3\35\3\35\5\35\u0178")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\5!\u018a\n!\3!\3!\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\7\"\u0195\n\"\f\"\16\"\u0198\13\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\5\"\u019f\n\"\3\"\3\"\3\"\3\"\3\"\7\"\u01a6")
        buf.write("\n\"\f\"\16\"\u01a9\13\"\3\"\3\"\3\"\5\"\u01ae\n\"\3#")
        buf.write("\3#\7#\u01b2\n#\f#\16#\u01b5\13#\3#\3#\3$\3$\3$\3$\3$")
        buf.write("\3%\3%\3%\2\t\32\34\36 \"(*&\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFH\2\b\4\2\25")
        buf.write("\25\31\31\4\2##%)\3\2!\"\3\2\33\34\4\2\35\37,,\3\2\r\20")
        buf.write("\2\u01d3\2K\3\2\2\2\4Q\3\2\2\2\6Z\3\2\2\2\b`\3\2\2\2\n")
        buf.write("e\3\2\2\2\fg\3\2\2\2\16\177\3\2\2\2\20\u0088\3\2\2\2\22")
        buf.write("\u0096\3\2\2\2\24\u009e\3\2\2\2\26\u00ae\3\2\2\2\30\u00b0")
        buf.write("\3\2\2\2\32\u00b2\3\2\2\2\34\u00bd\3\2\2\2\36\u00c8\3")
        buf.write("\2\2\2 \u00d3\3\2\2\2\"\u00de\3\2\2\2$\u00ec\3\2\2\2&")
        buf.write("\u00f1\3\2\2\2(\u00f3\3\2\2\2*\u0100\3\2\2\2,\u012b\3")
        buf.write("\2\2\2.\u013c\3\2\2\2\60\u0145\3\2\2\2\62\u0150\3\2\2")
        buf.write("\2\64\u0152\3\2\2\2\66\u016a\3\2\2\28\u016f\3\2\2\2:\u0179")
        buf.write("\3\2\2\2<\u0181\3\2\2\2>\u0184\3\2\2\2@\u0187\3\2\2\2")
        buf.write("B\u01ad\3\2\2\2D\u01af\3\2\2\2F\u01b8\3\2\2\2H\u01bd\3")
        buf.write("\2\2\2JL\5\4\3\2KJ\3\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2")
        buf.write("\2NO\3\2\2\2OP\7\2\2\3P\3\3\2\2\2QS\7\23\2\2RT\5\6\4\2")
        buf.write("SR\3\2\2\2ST\3\2\2\2TU\3\2\2\2UV\7>\2\2VW\7\63\2\2WX\5")
        buf.write("\b\5\2XY\7\64\2\2Y\5\3\2\2\2Z[\7>\2\2[\\\7\3\2\2\\\7\3")
        buf.write("\2\2\2]_\5\n\6\2^]\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2")
        buf.write("\2a\t\3\2\2\2b`\3\2\2\2cf\5\f\7\2df\5\20\t\2ec\3\2\2\2")
        buf.write("ed\3\2\2\2f\13\3\2\2\2gh\t\2\2\2hm\7@\2\2ij\7\62\2\2j")
        buf.write("l\7@\2\2ki\3\2\2\2lo\3\2\2\2mk\3\2\2\2mn\3\2\2\2np\3\2")
        buf.write("\2\2om\3\2\2\2pq\7\66\2\2q{\5\26\f\2rs\7$\2\2sx\5\30\r")
        buf.write("\2tu\7\62\2\2uw\5\30\r\2vt\3\2\2\2wz\3\2\2\2xv\3\2\2\2")
        buf.write("xy\3\2\2\2y|\3\2\2\2zx\3\2\2\2{r\3\2\2\2{|\3\2\2\2|}\3")
        buf.write("\2\2\2}~\7\65\2\2~\r\3\2\2\2\177\u0080\7\32\2\2\u0080")
        buf.write("\u0081\7\24\2\2\u0081\u0083\7\63\2\2\u0082\u0084\5\22")
        buf.write("\n\2\u0083\u0082\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0085")
        buf.write("\3\2\2\2\u0085\u0086\7\64\2\2\u0086\u0087\5D#\2\u0087")
        buf.write("\17\3\2\2\2\u0088\u0089\7\32\2\2\u0089\u008a\7@\2\2\u008a")
        buf.write("\u008c\7\63\2\2\u008b\u008d\5\22\n\2\u008c\u008b\3\2\2")
        buf.write("\2\u008c\u008d\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008f")
        buf.write("\7\64\2\2\u008f\u0092\7\66\2\2\u0090\u0093\5\26\f\2\u0091")
        buf.write("\u0093\7\30\2\2\u0092\u0090\3\2\2\2\u0092\u0091\3\2\2")
        buf.write("\2\u0093\u0094\3\2\2\2\u0094\u0095\5D#\2\u0095\21\3\2")
        buf.write("\2\2\u0096\u009b\5\24\13\2\u0097\u0098\7\62\2\2\u0098")
        buf.write("\u009a\5\24\13\2\u0099\u0097\3\2\2\2\u009a\u009d\3\2\2")
        buf.write("\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\23\3")
        buf.write("\2\2\2\u009d\u009b\3\2\2\2\u009e\u00a3\7>\2\2\u009f\u00a0")
        buf.write("\7\62\2\2\u00a0\u00a2\7>\2\2\u00a1\u009f\3\2\2\2\u00a2")
        buf.write("\u00a5\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2")
        buf.write("\u00a4\u00a6\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a7\7")
        buf.write("\66\2\2\u00a7\u00a8\5\26\f\2\u00a8\25\3\2\2\2\u00a9\u00af")
        buf.write("\7\17\2\2\u00aa\u00af\7\r\2\2\u00ab\u00af\7\16\2\2\u00ac")
        buf.write("\u00af\7\20\2\2\u00ad\u00af\5F$\2\u00ae\u00a9\3\2\2\2")
        buf.write("\u00ae\u00aa\3\2\2\2\u00ae\u00ab\3\2\2\2\u00ae\u00ac\3")
        buf.write("\2\2\2\u00ae\u00ad\3\2\2\2\u00af\27\3\2\2\2\u00b0\u00b1")
        buf.write("\5\32\16\2\u00b1\31\3\2\2\2\u00b2\u00b3\b\16\1\2\u00b3")
        buf.write("\u00b4\5\34\17\2\u00b4\u00ba\3\2\2\2\u00b5\u00b6\f\4\2")
        buf.write("\2\u00b6\u00b7\7+\2\2\u00b7\u00b9\5\34\17\2\u00b8\u00b5")
        buf.write("\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba")
        buf.write("\u00bb\3\2\2\2\u00bb\33\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd")
        buf.write("\u00be\b\17\1\2\u00be\u00bf\5\36\20\2\u00bf\u00c5\3\2")
        buf.write("\2\2\u00c0\u00c1\f\4\2\2\u00c1\u00c2\t\3\2\2\u00c2\u00c4")
        buf.write("\5\36\20\2\u00c3\u00c0\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5")
        buf.write("\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\35\3\2\2\2\u00c7")
        buf.write("\u00c5\3\2\2\2\u00c8\u00c9\b\20\1\2\u00c9\u00ca\5 \21")
        buf.write("\2\u00ca\u00d0\3\2\2\2\u00cb\u00cc\f\4\2\2\u00cc\u00cd")
        buf.write("\t\4\2\2\u00cd\u00cf\5 \21\2\u00ce\u00cb\3\2\2\2\u00cf")
        buf.write("\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2")
        buf.write("\u00d1\37\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00d4\b\21")
        buf.write("\1\2\u00d4\u00d5\5\"\22\2\u00d5\u00db\3\2\2\2\u00d6\u00d7")
        buf.write("\f\4\2\2\u00d7\u00d8\t\5\2\2\u00d8\u00da\5\"\22\2\u00d9")
        buf.write("\u00d6\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2")
        buf.write("\u00db\u00dc\3\2\2\2\u00dc!\3\2\2\2\u00dd\u00db\3\2\2")
        buf.write("\2\u00de\u00df\b\22\1\2\u00df\u00e0\5$\23\2\u00e0\u00e6")
        buf.write("\3\2\2\2\u00e1\u00e2\f\4\2\2\u00e2\u00e3\t\6\2\2\u00e3")
        buf.write("\u00e5\5$\23\2\u00e4\u00e1\3\2\2\2\u00e5\u00e8\3\2\2\2")
        buf.write("\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7#\3\2\2")
        buf.write("\2\u00e8\u00e6\3\2\2\2\u00e9\u00ea\7 \2\2\u00ea\u00ed")
        buf.write("\5&\24\2\u00eb\u00ed\5&\24\2\u00ec\u00e9\3\2\2\2\u00ec")
        buf.write("\u00eb\3\2\2\2\u00ed%\3\2\2\2\u00ee\u00ef\7\34\2\2\u00ef")
        buf.write("\u00f2\5(\25\2\u00f0\u00f2\5(\25\2\u00f1\u00ee\3\2\2\2")
        buf.write("\u00f1\u00f0\3\2\2\2\u00f2\'\3\2\2\2\u00f3\u00f4\b\25")
        buf.write("\1\2\u00f4\u00f5\5*\26\2\u00f5\u00fd\3\2\2\2\u00f6\u00f7")
        buf.write("\f\4\2\2\u00f7\u00f8\7/\2\2\u00f8\u00f9\5*\26\2\u00f9")
        buf.write("\u00fa\7\60\2\2\u00fa\u00fc\3\2\2\2\u00fb\u00f6\3\2\2")
        buf.write("\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe")
        buf.write("\3\2\2\2\u00fe)\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100\u0101")
        buf.write("\b\26\1\2\u0101\u0102\5,\27\2\u0102\u0115\3\2\2\2\u0103")
        buf.write("\u0104\f\4\2\2\u0104\u0105\7\61\2\2\u0105\u0111\7>\2\2")
        buf.write("\u0106\u0107\7-\2\2\u0107\u010c\5,\27\2\u0108\u0109\7")
        buf.write("\62\2\2\u0109\u010b\5,\27\2\u010a\u0108\3\2\2\2\u010b")
        buf.write("\u010e\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2")
        buf.write("\u010d\u010f\3\2\2\2\u010e\u010c\3\2\2\2\u010f\u0110\7")
        buf.write(".\2\2\u0110\u0112\3\2\2\2\u0111\u0106\3\2\2\2\u0111\u0112")
        buf.write("\3\2\2\2\u0112\u0114\3\2\2\2\u0113\u0103\3\2\2\2\u0114")
        buf.write("\u0117\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116\3\2\2\2")
        buf.write("\u0116+\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u0119\7>\2\2")
        buf.write("\u0119\u011b\7\61\2\2\u011a\u0118\3\2\2\2\u011a\u011b")
        buf.write("\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u0128\7?\2\2\u011d")
        buf.write("\u011e\7-\2\2\u011e\u0123\5.\30\2\u011f\u0120\7\62\2\2")
        buf.write("\u0120\u0122\5.\30\2\u0121\u011f\3\2\2\2\u0122\u0125\3")
        buf.write("\2\2\2\u0123\u0121\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0126")
        buf.write("\3\2\2\2\u0125\u0123\3\2\2\2\u0126\u0127\7.\2\2\u0127")
        buf.write("\u0129\3\2\2\2\u0128\u011d\3\2\2\2\u0128\u0129\3\2\2\2")
        buf.write("\u0129\u012c\3\2\2\2\u012a\u012c\5.\30\2\u012b\u011a\3")
        buf.write("\2\2\2\u012b\u012a\3\2\2\2\u012c-\3\2\2\2\u012d\u012e")
        buf.write("\7\27\2\2\u012e\u012f\7>\2\2\u012f\u0138\7-\2\2\u0130")
        buf.write("\u0135\5\60\31\2\u0131\u0132\7\62\2\2\u0132\u0134\5\60")
        buf.write("\31\2\u0133\u0131\3\2\2\2\u0134\u0137\3\2\2\2\u0135\u0133")
        buf.write("\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0139\3\2\2\2\u0137")
        buf.write("\u0135\3\2\2\2\u0138\u0130\3\2\2\2\u0138\u0139\3\2\2\2")
        buf.write("\u0139\u013a\3\2\2\2\u013a\u013d\7.\2\2\u013b\u013d\5")
        buf.write("\60\31\2\u013c\u012d\3\2\2\2\u013c\u013b\3\2\2\2\u013d")
        buf.write("/\3\2\2\2\u013e\u0146\7\67\2\2\u013f\u0146\7\26\2\2\u0140")
        buf.write("\u0146\7>\2\2\u0141\u0142\7\63\2\2\u0142\u0143\5\30\r")
        buf.write("\2\u0143\u0144\7\64\2\2\u0144\u0146\3\2\2\2\u0145\u013e")
        buf.write("\3\2\2\2\u0145\u013f\3\2\2\2\u0145\u0140\3\2\2\2\u0145")
        buf.write("\u0141\3\2\2\2\u0146\61\3\2\2\2\u0147\u0151\5\64\33\2")
        buf.write("\u0148\u0151\5\66\34\2\u0149\u0151\58\35\2\u014a\u0151")
        buf.write("\5:\36\2\u014b\u0151\5<\37\2\u014c\u0151\5> \2\u014d\u0151")
        buf.write("\5@!\2\u014e\u0151\5B\"\2\u014f\u0151\5D#\2\u0150\u0147")
        buf.write("\3\2\2\2\u0150\u0148\3\2\2\2\u0150\u0149\3\2\2\2\u0150")
        buf.write("\u014a\3\2\2\2\u0150\u014b\3\2\2\2\u0150\u014c\3\2\2\2")
        buf.write("\u0150\u014d\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u014f\3")
        buf.write("\2\2\2\u0151\63\3\2\2\2\u0152\u0153\t\2\2\2\u0153\u0158")
        buf.write("\7>\2\2\u0154\u0155\7\62\2\2\u0155\u0157\7>\2\2\u0156")
        buf.write("\u0154\3\2\2\2\u0157\u015a\3\2\2\2\u0158\u0156\3\2\2\2")
        buf.write("\u0158\u0159\3\2\2\2\u0159\u015b\3\2\2\2\u015a\u0158\3")
        buf.write("\2\2\2\u015b\u015c\7\66\2\2\u015c\u0166\5\26\f\2\u015d")
        buf.write("\u015e\7$\2\2\u015e\u0163\5\30\r\2\u015f\u0160\7\62\2")
        buf.write("\2\u0160\u0162\5\30\r\2\u0161\u015f\3\2\2\2\u0162\u0165")
        buf.write("\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164")
        buf.write("\u0167\3\2\2\2\u0165\u0163\3\2\2\2\u0166\u015d\3\2\2\2")
        buf.write("\u0166\u0167\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0169\7")
        buf.write("\65\2\2\u0169\65\3\2\2\2\u016a\u016b\5\30\r\2\u016b\u016c")
        buf.write("\7*\2\2\u016c\u016d\5\30\r\2\u016d\u016e\7\65\2\2\u016e")
        buf.write("\67\3\2\2\2\u016f\u0171\7\b\2\2\u0170\u0172\5D#\2\u0171")
        buf.write("\u0170\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0173\3\2\2\2")
        buf.write("\u0173\u0174\5\30\r\2\u0174\u0177\5D#\2\u0175\u0176\7")
        buf.write("\t\2\2\u0176\u0178\5D#\2\u0177\u0175\3\2\2\2\u0177\u0178")
        buf.write("\3\2\2\2\u01789\3\2\2\2\u0179\u017a\7\n\2\2\u017a\u017b")
        buf.write("\5\66\34\2\u017b\u017c\7\65\2\2\u017c\u017d\5\30\r\2\u017d")
        buf.write("\u017e\7\65\2\2\u017e\u017f\5\66\34\2\u017f\u0180\5D#")
        buf.write("\2\u0180;\3\2\2\2\u0181\u0182\7\6\2\2\u0182\u0183\7\65")
        buf.write("\2\2\u0183=\3\2\2\2\u0184\u0185\7\7\2\2\u0185\u0186\7")
        buf.write("\65\2\2\u0186?\3\2\2\2\u0187\u0189\7\21\2\2\u0188\u018a")
        buf.write("\5\30\r\2\u0189\u0188\3\2\2\2\u0189\u018a\3\2\2\2\u018a")
        buf.write("\u018b\3\2\2\2\u018b\u018c\7\65\2\2\u018cA\3\2\2\2\u018d")
        buf.write("\u018e\5\30\r\2\u018e\u018f\7\61\2\2\u018f\u0190\7>\2")
        buf.write("\2\u0190\u0191\7-\2\2\u0191\u0196\5\30\r\2\u0192\u0193")
        buf.write("\7\62\2\2\u0193\u0195\5\30\r\2\u0194\u0192\3\2\2\2\u0195")
        buf.write("\u0198\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2")
        buf.write("\u0197\u0199\3\2\2\2\u0198\u0196\3\2\2\2\u0199\u019a\7")
        buf.write(".\2\2\u019a\u019b\7\65\2\2\u019b\u01ae\3\2\2\2\u019c\u019d")
        buf.write("\7>\2\2\u019d\u019f\7\61\2\2\u019e\u019c\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1\7?\2\2")
        buf.write("\u01a1\u01a2\7-\2\2\u01a2\u01a7\5\30\r\2\u01a3\u01a4\7")
        buf.write("\62\2\2\u01a4\u01a6\5\30\r\2\u01a5\u01a3\3\2\2\2\u01a6")
        buf.write("\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2")
        buf.write("\u01a8\u01aa\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa\u01ab\7")
        buf.write(".\2\2\u01ab\u01ac\7\65\2\2\u01ac\u01ae\3\2\2\2\u01ad\u018d")
        buf.write("\3\2\2\2\u01ad\u019e\3\2\2\2\u01aeC\3\2\2\2\u01af\u01b3")
        buf.write("\7\63\2\2\u01b0\u01b2\5\62\32\2\u01b1\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b5\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2")
        buf.write("\u01b4\u01b6\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6\u01b7\7")
        buf.write("\64\2\2\u01b7E\3\2\2\2\u01b8\u01b9\7/\2\2\u01b9\u01ba")
        buf.write("\7:\2\2\u01ba\u01bb\7\60\2\2\u01bb\u01bc\5H%\2\u01bcG")
        buf.write("\3\2\2\2\u01bd\u01be\t\7\2\2\u01beI\3\2\2\2.MS`emx{\u0083")
        buf.write("\u008c\u0092\u009b\u00a3\u00ae\u00ba\u00c5\u00d0\u00db")
        buf.write("\u00e6\u00ec\u00f1\u00fd\u010c\u0111\u0115\u011a\u0123")
        buf.write("\u0128\u012b\u0135\u0138\u013c\u0145\u0150\u0158\u0163")
        buf.write("\u0166\u0171\u0177\u0189\u0196\u019e\u01a7\u01ad\u01b3")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<-'", "<INVALID>", "<INVALID>", "'break'", 
                     "'continue'", "'if'", "'else'", "'for'", "'true'", 
                     "'false'", "'int'", "'float'", "'bool'", "'string'", 
                     "'return'", "'null'", "'class'", "'constructor'", "'var'", 
                     "'self'", "'new'", "'void'", "'const'", "'func'", "'+'", 
                     "'-'", "'*'", "'/'", "'\\'", "'!'", "'&&'", "'||'", 
                     "'=='", "'='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "':='", "'^'", "'%'", "'('", "')'", "'['", "']'", "'.'", 
                     "','", "'{'", "'}'", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", 
                      "FALSE", "INT", "FLOAT", "BOOL", "STRING", "RETURN", 
                      "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", 
                      "VOID", "CONST", "FUNC", "ADD_OP", "SUB_OP", "MUL_OP", 
                      "DIV_OP", "BACKSLASH", "NEGATE", "AND", "OR", "EQUAL", 
                      "ASSIGN_OP", "NOT_EQUAL", "LESS_THAN", "LESS_EQUAL", 
                      "GREATER_THAN", "GREATER_EQUAL", "DECLARE_ASSIGN_OP", 
                      "POW_OP", "MOD_OP", "LB", "RB", "LS", "RS", "DOT", 
                      "CM", "LP", "RP", "SEMI", "COLON", "LIT", "LIT_EXCEPT_ARRAY", 
                      "FLOAT_LIT", "INT_LIT", "BOOL_LIT", "STRING_LIT", 
                      "ARRAY_LIT", "ID", "AT_ID", "MEMBER_ID", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_dcl = 1
    RULE_class_super = 2
    RULE_class_body = 3
    RULE_class_member = 4
    RULE_attribute = 5
    RULE_constructor_method = 6
    RULE_method = 7
    RULE_param_list = 8
    RULE_param = 9
    RULE_data_type = 10
    RULE_expr = 11
    RULE_expr_string = 12
    RULE_expr_rela = 13
    RULE_expr_logic = 14
    RULE_expr_add = 15
    RULE_expr_multi = 16
    RULE_expr_logic_not = 17
    RULE_expr_sign = 18
    RULE_expr_index_op = 19
    RULE_expr_instance_access = 20
    RULE_expr_static_access = 21
    RULE_expr_object_creation = 22
    RULE_expr_term = 23
    RULE_stmt = 24
    RULE_dcl_stmt = 25
    RULE_assign_stmt = 26
    RULE_if_stmt = 27
    RULE_for_stmt = 28
    RULE_break_stmt = 29
    RULE_continue_stmt = 30
    RULE_return_stmt = 31
    RULE_method_invocation_stmt = 32
    RULE_block_stmt = 33
    RULE_array_type = 34
    RULE_element_type = 35

    ruleNames =  [ "program", "class_dcl", "class_super", "class_body", 
                   "class_member", "attribute", "constructor_method", "method", 
                   "param_list", "param", "data_type", "expr", "expr_string", 
                   "expr_rela", "expr_logic", "expr_add", "expr_multi", 
                   "expr_logic_not", "expr_sign", "expr_index_op", "expr_instance_access", 
                   "expr_static_access", "expr_object_creation", "expr_term", 
                   "stmt", "dcl_stmt", "assign_stmt", "if_stmt", "for_stmt", 
                   "break_stmt", "continue_stmt", "return_stmt", "method_invocation_stmt", 
                   "block_stmt", "array_type", "element_type" ]

    EOF = Token.EOF
    T__0=1
    LINE_COMMENT=2
    BLOCK_COMMENT=3
    BREAK=4
    CONTINUE=5
    IF=6
    ELSE=7
    FOR=8
    TRUE=9
    FALSE=10
    INT=11
    FLOAT=12
    BOOL=13
    STRING=14
    RETURN=15
    NULL=16
    CLASS=17
    CONSTRUCTOR=18
    VAR=19
    SELF=20
    NEW=21
    VOID=22
    CONST=23
    FUNC=24
    ADD_OP=25
    SUB_OP=26
    MUL_OP=27
    DIV_OP=28
    BACKSLASH=29
    NEGATE=30
    AND=31
    OR=32
    EQUAL=33
    ASSIGN_OP=34
    NOT_EQUAL=35
    LESS_THAN=36
    LESS_EQUAL=37
    GREATER_THAN=38
    GREATER_EQUAL=39
    DECLARE_ASSIGN_OP=40
    POW_OP=41
    MOD_OP=42
    LB=43
    RB=44
    LS=45
    RS=46
    DOT=47
    CM=48
    LP=49
    RP=50
    SEMI=51
    COLON=52
    LIT=53
    LIT_EXCEPT_ARRAY=54
    FLOAT_LIT=55
    INT_LIT=56
    BOOL_LIT=57
    STRING_LIT=58
    ARRAY_LIT=59
    ID=60
    AT_ID=61
    MEMBER_ID=62
    WS=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65
    ERROR_CHAR=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CSlangParser.EOF, 0)

        def class_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Class_dclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Class_dclContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 72
                self.class_dcl()
                self.state = 75 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSlangParser.CLASS):
                    break

            self.state = 77
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_dclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CSlangParser.CLASS, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def class_body(self):
            return self.getTypedRuleContext(CSlangParser.Class_bodyContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def class_super(self):
            return self.getTypedRuleContext(CSlangParser.Class_superContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_dcl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_dcl" ):
                return visitor.visitClass_dcl(self)
            else:
                return visitor.visitChildren(self)




    def class_dcl(self):

        localctx = CSlangParser.Class_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_dcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(CSlangParser.CLASS)
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 80
                self.class_super()


            self.state = 83
            self.match(CSlangParser.ID)
            self.state = 84
            self.match(CSlangParser.LP)
            self.state = 85
            self.class_body()
            self.state = 86
            self.match(CSlangParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_superContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_class_super

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_super" ):
                return visitor.visitClass_super(self)
            else:
                return visitor.visitChildren(self)




    def class_super(self):

        localctx = CSlangParser.Class_superContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_super)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(CSlangParser.ID)
            self.state = 89
            self.match(CSlangParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Class_memberContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Class_memberContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body" ):
                return visitor.visitClass_body(self)
            else:
                return visitor.visitChildren(self)




    def class_body(self):

        localctx = CSlangParser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.VAR) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC))) != 0):
                self.state = 91
                self.class_member()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_memberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(CSlangParser.AttributeContext,0)


        def method(self):
            return self.getTypedRuleContext(CSlangParser.MethodContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_member" ):
                return visitor.visitClass_member(self)
            else:
                return visitor.visitChildren(self)




    def class_member(self):

        localctx = CSlangParser.Class_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_member)
        try:
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.attribute()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.method()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(CSlangParser.Data_typeContext,0)


        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def MEMBER_ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.MEMBER_ID)
            else:
                return self.getToken(CSlangParser.MEMBER_ID, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def ASSIGN_OP(self):
            return self.getToken(CSlangParser.ASSIGN_OP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = CSlangParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()

            self.state = 102
            self.match(CSlangParser.MEMBER_ID)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 103
                self.match(CSlangParser.CM)
                self.state = 104
                self.match(CSlangParser.MEMBER_ID)
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
            self.match(CSlangParser.COLON)
            self.state = 111
            self.data_type()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ASSIGN_OP:
                self.state = 112
                self.match(CSlangParser.ASSIGN_OP)
                self.state = 113
                self.expr()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSlangParser.CM:
                    self.state = 114
                    self.match(CSlangParser.CM)
                    self.state = 115
                    self.expr()
                    self.state = 120
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 123
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def CONSTRUCTOR(self):
            return self.getToken(CSlangParser.CONSTRUCTOR, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def param_list(self):
            return self.getTypedRuleContext(CSlangParser.Param_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constructor_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_method" ):
                return visitor.visitConstructor_method(self)
            else:
                return visitor.visitChildren(self)




    def constructor_method(self):

        localctx = CSlangParser.Constructor_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_constructor_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(CSlangParser.FUNC)
            self.state = 126
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 127
            self.match(CSlangParser.LP)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 128
                self.param_list()


            self.state = 131
            self.match(CSlangParser.RP)
            self.state = 132
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def MEMBER_ID(self):
            return self.getToken(CSlangParser.MEMBER_ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def data_type(self):
            return self.getTypedRuleContext(CSlangParser.Data_typeContext,0)


        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def param_list(self):
            return self.getTypedRuleContext(CSlangParser.Param_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = CSlangParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(CSlangParser.FUNC)
            self.state = 135
            self.match(CSlangParser.MEMBER_ID)
            self.state = 136
            self.match(CSlangParser.LP)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 137
                self.param_list()


            self.state = 140
            self.match(CSlangParser.RP)
            self.state = 141
            self.match(CSlangParser.COLON)
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.LS]:
                self.state = 142
                self.data_type()
                pass
            elif token in [CSlangParser.VOID]:
                self.state = 143
                self.match(CSlangParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 146
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ParamContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ParamContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = CSlangParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.param()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 149
                self.match(CSlangParser.CM)
                self.state = 150
                self.param()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.ID)
            else:
                return self.getToken(CSlangParser.ID, i)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(CSlangParser.Data_typeContext,0)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = CSlangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(CSlangParser.ID)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 157
                self.match(CSlangParser.CM)
                self.state = 158
                self.match(CSlangParser.ID)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 164
            self.match(CSlangParser.COLON)
            self.state = 165
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def array_type(self):
            return self.getTypedRuleContext(CSlangParser.Array_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = CSlangParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_data_type)
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.BOOL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(CSlangParser.BOOL)
                pass
            elif token in [CSlangParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(CSlangParser.INT)
                pass
            elif token in [CSlangParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 169
                self.match(CSlangParser.FLOAT)
                pass
            elif token in [CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 170
                self.match(CSlangParser.STRING)
                pass
            elif token in [CSlangParser.LS]:
                self.enterOuterAlt(localctx, 5)
                self.state = 171
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_string(self):
            return self.getTypedRuleContext(CSlangParser.Expr_stringContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CSlangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.expr_string(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_rela(self):
            return self.getTypedRuleContext(CSlangParser.Expr_relaContext,0)


        def expr_string(self):
            return self.getTypedRuleContext(CSlangParser.Expr_stringContext,0)


        def POW_OP(self):
            return self.getToken(CSlangParser.POW_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_string" ):
                return visitor.visitExpr_string(self)
            else:
                return visitor.visitChildren(self)



    def expr_string(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr_stringContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr_string, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.expr_rela(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 184
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr_stringContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_string)
                    self.state = 179
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 180
                    self.match(CSlangParser.POW_OP)
                    self.state = 181
                    self.expr_rela(0) 
                self.state = 186
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_relaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_logic(self):
            return self.getTypedRuleContext(CSlangParser.Expr_logicContext,0)


        def expr_rela(self):
            return self.getTypedRuleContext(CSlangParser.Expr_relaContext,0)


        def EQUAL(self):
            return self.getToken(CSlangParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(CSlangParser.NOT_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(CSlangParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(CSlangParser.GREATER_THAN, 0)

        def LESS_EQUAL(self):
            return self.getToken(CSlangParser.LESS_EQUAL, 0)

        def GREATER_EQUAL(self):
            return self.getToken(CSlangParser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr_rela

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_rela" ):
                return visitor.visitExpr_rela(self)
            else:
                return visitor.visitChildren(self)



    def expr_rela(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr_relaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr_rela, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.expr_logic(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 195
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr_relaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_rela)
                    self.state = 190
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 191
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQUAL) | (1 << CSlangParser.NOT_EQUAL) | (1 << CSlangParser.LESS_THAN) | (1 << CSlangParser.LESS_EQUAL) | (1 << CSlangParser.GREATER_THAN) | (1 << CSlangParser.GREATER_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 192
                    self.expr_logic(0) 
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_logicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_add(self):
            return self.getTypedRuleContext(CSlangParser.Expr_addContext,0)


        def expr_logic(self):
            return self.getTypedRuleContext(CSlangParser.Expr_logicContext,0)


        def AND(self):
            return self.getToken(CSlangParser.AND, 0)

        def OR(self):
            return self.getToken(CSlangParser.OR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr_logic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_logic" ):
                return visitor.visitExpr_logic(self)
            else:
                return visitor.visitChildren(self)



    def expr_logic(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr_logicContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr_logic, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.expr_add(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 206
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr_logicContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_logic)
                    self.state = 201
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 202
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.AND or _la==CSlangParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 203
                    self.expr_add(0) 
                self.state = 208
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_addContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_multi(self):
            return self.getTypedRuleContext(CSlangParser.Expr_multiContext,0)


        def expr_add(self):
            return self.getTypedRuleContext(CSlangParser.Expr_addContext,0)


        def ADD_OP(self):
            return self.getToken(CSlangParser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(CSlangParser.SUB_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr_add

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_add" ):
                return visitor.visitExpr_add(self)
            else:
                return visitor.visitChildren(self)



    def expr_add(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr_addContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr_add, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.expr_multi(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 217
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr_addContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_add)
                    self.state = 212
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 213
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.ADD_OP or _la==CSlangParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 214
                    self.expr_multi(0) 
                self.state = 219
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_multiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_logic_not(self):
            return self.getTypedRuleContext(CSlangParser.Expr_logic_notContext,0)


        def expr_multi(self):
            return self.getTypedRuleContext(CSlangParser.Expr_multiContext,0)


        def MUL_OP(self):
            return self.getToken(CSlangParser.MUL_OP, 0)

        def DIV_OP(self):
            return self.getToken(CSlangParser.DIV_OP, 0)

        def BACKSLASH(self):
            return self.getToken(CSlangParser.BACKSLASH, 0)

        def MOD_OP(self):
            return self.getToken(CSlangParser.MOD_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr_multi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_multi" ):
                return visitor.visitExpr_multi(self)
            else:
                return visitor.visitChildren(self)



    def expr_multi(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr_multiContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr_multi, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.expr_logic_not()
            self._ctx.stop = self._input.LT(-1)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr_multiContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_multi)
                    self.state = 223
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 224
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MUL_OP) | (1 << CSlangParser.DIV_OP) | (1 << CSlangParser.BACKSLASH) | (1 << CSlangParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 225
                    self.expr_logic_not() 
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_logic_notContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEGATE(self):
            return self.getToken(CSlangParser.NEGATE, 0)

        def expr_sign(self):
            return self.getTypedRuleContext(CSlangParser.Expr_signContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr_logic_not

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_logic_not" ):
                return visitor.visitExpr_logic_not(self)
            else:
                return visitor.visitChildren(self)




    def expr_logic_not(self):

        localctx = CSlangParser.Expr_logic_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr_logic_not)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEGATE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(CSlangParser.NEGATE)
                self.state = 232
                self.expr_sign()
                pass
            elif token in [CSlangParser.SELF, CSlangParser.NEW, CSlangParser.SUB_OP, CSlangParser.LP, CSlangParser.LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.expr_sign()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_signContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_OP(self):
            return self.getToken(CSlangParser.SUB_OP, 0)

        def expr_index_op(self):
            return self.getTypedRuleContext(CSlangParser.Expr_index_opContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr_sign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_sign" ):
                return visitor.visitExpr_sign(self)
            else:
                return visitor.visitChildren(self)




    def expr_sign(self):

        localctx = CSlangParser.Expr_signContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr_sign)
        try:
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SUB_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(CSlangParser.SUB_OP)
                self.state = 237
                self.expr_index_op(0)
                pass
            elif token in [CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LP, CSlangParser.LIT, CSlangParser.ID, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.expr_index_op(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_index_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_instance_access(self):
            return self.getTypedRuleContext(CSlangParser.Expr_instance_accessContext,0)


        def expr_index_op(self):
            return self.getTypedRuleContext(CSlangParser.Expr_index_opContext,0)


        def LS(self):
            return self.getToken(CSlangParser.LS, 0)

        def RS(self):
            return self.getToken(CSlangParser.RS, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_index_op" ):
                return visitor.visitExpr_index_op(self)
            else:
                return visitor.visitChildren(self)



    def expr_index_op(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr_index_opContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr_index_op, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.expr_instance_access(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 251
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr_index_opContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_index_op)
                    self.state = 244
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 245
                    self.match(CSlangParser.LS)
                    self.state = 246
                    self.expr_instance_access(0)
                    self.state = 247
                    self.match(CSlangParser.RS) 
                self.state = 253
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_instance_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_static_access(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr_static_accessContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr_static_accessContext,i)


        def expr_instance_access(self):
            return self.getTypedRuleContext(CSlangParser.Expr_instance_accessContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr_instance_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_instance_access" ):
                return visitor.visitExpr_instance_access(self)
            else:
                return visitor.visitChildren(self)



    def expr_instance_access(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr_instance_accessContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr_instance_access, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.expr_static_access()
            self._ctx.stop = self._input.LT(-1)
            self.state = 275
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr_instance_accessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_instance_access)
                    self.state = 257
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 258
                    self.match(CSlangParser.DOT)
                    self.state = 259
                    self.match(CSlangParser.ID)
                    self.state = 271
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        self.state = 260
                        self.match(CSlangParser.LB)
                        self.state = 261
                        self.expr_static_access()
                        self.state = 266
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==CSlangParser.CM:
                            self.state = 262
                            self.match(CSlangParser.CM)
                            self.state = 263
                            self.expr_static_access()
                            self.state = 268
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 269
                        self.match(CSlangParser.RB)

             
                self.state = 277
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_static_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def expr_object_creation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr_object_creationContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr_object_creationContext,i)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr_static_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_static_access" ):
                return visitor.visitExpr_static_access(self)
            else:
                return visitor.visitChildren(self)




    def expr_static_access(self):

        localctx = CSlangParser.Expr_static_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr_static_access)
        self._la = 0 # Token type
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 278
                    self.match(CSlangParser.ID)
                    self.state = 279
                    self.match(CSlangParser.DOT)


                self.state = 282
                self.match(CSlangParser.AT_ID)
                self.state = 294
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 283
                    self.match(CSlangParser.LB)
                    self.state = 284
                    self.expr_object_creation()
                    self.state = 289
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==CSlangParser.CM:
                        self.state = 285
                        self.match(CSlangParser.CM)
                        self.state = 286
                        self.expr_object_creation()
                        self.state = 291
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 292
                    self.match(CSlangParser.RB)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.expr_object_creation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_object_creationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def expr_term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr_termContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr_termContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr_object_creation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_object_creation" ):
                return visitor.visitExpr_object_creation(self)
            else:
                return visitor.visitChildren(self)




    def expr_object_creation(self):

        localctx = CSlangParser.Expr_object_creationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr_object_creation)
        self._la = 0 # Token type
        try:
            self.state = 314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(CSlangParser.NEW)
                self.state = 300
                self.match(CSlangParser.ID)
                self.state = 301
                self.match(CSlangParser.LB)
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.SELF) | (1 << CSlangParser.LP) | (1 << CSlangParser.LIT) | (1 << CSlangParser.ID))) != 0):
                    self.state = 302
                    self.expr_term()
                    self.state = 307
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==CSlangParser.CM:
                        self.state = 303
                        self.match(CSlangParser.CM)
                        self.state = 304
                        self.expr_term()
                        self.state = 309
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 312
                self.match(CSlangParser.RB)
                pass
            elif token in [CSlangParser.SELF, CSlangParser.LP, CSlangParser.LIT, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.expr_term()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_termContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIT(self):
            return self.getToken(CSlangParser.LIT, 0)

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_term" ):
                return visitor.visitExpr_term(self)
            else:
                return visitor.visitChildren(self)




    def expr_term(self):

        localctx = CSlangParser.Expr_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr_term)
        try:
            self.state = 323
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(CSlangParser.LIT)
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.match(CSlangParser.SELF)
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 318
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.LP]:
                self.enterOuterAlt(localctx, 4)
                self.state = 319
                self.match(CSlangParser.LP)
                self.state = 320
                self.expr()
                self.state = 321
                self.match(CSlangParser.RP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dcl_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Dcl_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(CSlangParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(CSlangParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Return_stmtContext,0)


        def method_invocation_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Method_invocation_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_stmt)
        try:
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.dcl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 327
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 328
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 329
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 330
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 331
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 332
                self.method_invocation_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 333
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dcl_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(CSlangParser.Data_typeContext,0)


        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.ID)
            else:
                return self.getToken(CSlangParser.ID, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def ASSIGN_OP(self):
            return self.getToken(CSlangParser.ASSIGN_OP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_dcl_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDcl_stmt" ):
                return visitor.visitDcl_stmt(self)
            else:
                return visitor.visitChildren(self)




    def dcl_stmt(self):

        localctx = CSlangParser.Dcl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_dcl_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()

            self.state = 337
            self.match(CSlangParser.ID)
            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 338
                self.match(CSlangParser.CM)
                self.state = 339
                self.match(CSlangParser.ID)
                self.state = 344
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 345
            self.match(CSlangParser.COLON)
            self.state = 346
            self.data_type()
            self.state = 356
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ASSIGN_OP:
                self.state = 347
                self.match(CSlangParser.ASSIGN_OP)
                self.state = 348
                self.expr()
                self.state = 353
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSlangParser.CM:
                    self.state = 349
                    self.match(CSlangParser.CM)
                    self.state = 350
                    self.expr()
                    self.state = 355
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 358
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprContext,i)


        def DECLARE_ASSIGN_OP(self):
            return self.getToken(CSlangParser.DECLARE_ASSIGN_OP, 0)

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = CSlangParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.expr()
            self.state = 361
            self.match(CSlangParser.DECLARE_ASSIGN_OP)
            self.state = 362
            self.expr()
            self.state = 363
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CSlangParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Block_stmtContext,i)


        def ELSE(self):
            return self.getToken(CSlangParser.ELSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = CSlangParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(CSlangParser.IF)
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 366
                self.block_stmt()


            self.state = 369
            self.expr()
            self.state = 370
            self.block_stmt()
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 371
                self.match(CSlangParser.ELSE)
                self.state = 372
                self.block_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSlangParser.FOR, 0)

        def assign_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Assign_stmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Assign_stmtContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.SEMI)
            else:
                return self.getToken(CSlangParser.SEMI, i)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = CSlangParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(CSlangParser.FOR)
            self.state = 376
            self.assign_stmt()
            self.state = 377
            self.match(CSlangParser.SEMI)
            self.state = 378
            self.expr()
            self.state = 379
            self.match(CSlangParser.SEMI)
            self.state = 380
            self.assign_stmt()
            self.state = 381
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(CSlangParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = CSlangParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(CSlangParser.BREAK)
            self.state = 384
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(CSlangParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = CSlangParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(CSlangParser.CONTINUE)
            self.state = 387
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CSlangParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = CSlangParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(CSlangParser.RETURN)
            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NEGATE) | (1 << CSlangParser.LP) | (1 << CSlangParser.LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 390
                self.expr()


            self.state = 393
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocation_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprContext,i)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_method_invocation_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_stmt" ):
                return visitor.visitMethod_invocation_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_stmt(self):

        localctx = CSlangParser.Method_invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_method_invocation_stmt)
        self._la = 0 # Token type
        try:
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.expr()
                self.state = 396
                self.match(CSlangParser.DOT)
                self.state = 397
                self.match(CSlangParser.ID)
                self.state = 398
                self.match(CSlangParser.LB)
                self.state = 399
                self.expr()
                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSlangParser.CM:
                    self.state = 400
                    self.match(CSlangParser.CM)
                    self.state = 401
                    self.expr()
                    self.state = 406
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 407
                self.match(CSlangParser.RB)
                self.state = 408
                self.match(CSlangParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 410
                    self.match(CSlangParser.ID)
                    self.state = 411
                    self.match(CSlangParser.DOT)


                self.state = 414
                self.match(CSlangParser.AT_ID)
                self.state = 415
                self.match(CSlangParser.LB)
                self.state = 416
                self.expr()
                self.state = 421
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSlangParser.CM:
                    self.state = 417
                    self.match(CSlangParser.CM)
                    self.state = 418
                    self.expr()
                    self.state = 423
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 424
                self.match(CSlangParser.RB)
                self.state = 425
                self.match(CSlangParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.StmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.StmtContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = CSlangParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(CSlangParser.LP)
            self.state = 433
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.VAR) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.CONST) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NEGATE) | (1 << CSlangParser.LP) | (1 << CSlangParser.LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 430
                self.stmt()
                self.state = 435
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 436
            self.match(CSlangParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(CSlangParser.LS, 0)

        def INT_LIT(self):
            return self.getToken(CSlangParser.INT_LIT, 0)

        def RS(self):
            return self.getToken(CSlangParser.RS, 0)

        def element_type(self):
            return self.getTypedRuleContext(CSlangParser.Element_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = CSlangParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(CSlangParser.LS)
            self.state = 439
            self.match(CSlangParser.INT_LIT)
            self.state = 440
            self.match(CSlangParser.RS)
            self.state = 441
            self.element_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_element_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_type" ):
                return visitor.visitElement_type(self)
            else:
                return visitor.visitChildren(self)




    def element_type(self):

        localctx = CSlangParser.Element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_element_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.INT) | (1 << CSlangParser.FLOAT) | (1 << CSlangParser.BOOL) | (1 << CSlangParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expr_string_sempred
        self._predicates[13] = self.expr_rela_sempred
        self._predicates[14] = self.expr_logic_sempred
        self._predicates[15] = self.expr_add_sempred
        self._predicates[16] = self.expr_multi_sempred
        self._predicates[19] = self.expr_index_op_sempred
        self._predicates[20] = self.expr_instance_access_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_string_sempred(self, localctx:Expr_stringContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_rela_sempred(self, localctx:Expr_relaContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr_logic_sempred(self, localctx:Expr_logicContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr_add_sempred(self, localctx:Expr_addContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr_multi_sempred(self, localctx:Expr_multiContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr_index_op_sempred(self, localctx:Expr_index_opContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expr_instance_access_sempred(self, localctx:Expr_instance_accessContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




