# Generated from /Users/hoang/Projects/CO3005_Assignments/assignment1/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u0161\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\3\2\6\2@\n\2\r\2\16\2A\3\2\3\2\3\3\3\3\5\3")
        buf.write("H\n\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\7\5S\n\5\f\5")
        buf.write("\16\5V\13\5\3\6\3\6\3\6\5\6[\n\6\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\5\bc\n\b\3\t\3\t\3\t\7\th\n\t\f\t\16\tk\13\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\5\13~\n\13\3\f\3\f\3\f\3\f\5\f\u0084")
        buf.write("\n\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u008d\n\r\3\r\3\r")
        buf.write("\3\r\3\r\5\r\u0093\n\r\3\r\3\r\3\16\3\16\3\16\7\16\u009a")
        buf.write("\n\16\f\16\16\16\u009d\13\16\3\17\3\17\3\17\7\17\u00a2")
        buf.write("\n\17\f\17\16\17\u00a5\13\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\5\20\u00ac\n\20\3\20\3\20\7\20\u00b0\n\20\f\20\16\20")
        buf.write("\u00b3\13\20\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\5\22\u00c2\n\22\3\22\3\22\3\22")
        buf.write("\5\22\u00c7\n\22\3\22\3\22\3\22\5\22\u00cc\n\22\3\22\5")
        buf.write("\22\u00cf\n\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\5\22\u00dc\n\22\3\22\3\22\5\22\u00e0\n")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22")
        buf.write("\u00f6\n\22\3\22\5\22\u00f9\n\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\7\22\u0100\n\22\f\22\16\22\u0103\13\22\3\23\3\23\3")
        buf.write("\23\7\23\u0108\n\23\f\23\16\23\u010b\13\23\3\24\3\24\3")
        buf.write("\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\5\27\u0118")
        buf.write("\n\27\3\27\3\27\3\27\3\27\5\27\u011e\n\27\3\30\3\30\3")
        buf.write("\30\5\30\u0123\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\5\34\u0135")
        buf.write("\n\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\5\35\u013e\n")
        buf.write("\35\3\35\3\35\3\35\3\35\5\35\u0144\n\35\3\35\3\35\3\35")
        buf.write("\5\35\u0149\n\35\3\35\5\35\u014c\n\35\3\36\3\36\3\36\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u015a")
        buf.write("\n\37\f\37\16\37\u015d\13\37\3\37\3\37\3\37\2\3\" \2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<\2\n\4\2\25\25\31\31\3\2;<\4\2\13\f\679\4\2\r\20")
        buf.write(":;\4\2\35\37,,\3\2\33\34\3\2\"#\5\2  $$\'*\2\u017d\2?")
        buf.write("\3\2\2\2\4E\3\2\2\2\6N\3\2\2\2\bT\3\2\2\2\nZ\3\2\2\2\f")
        buf.write("\\\3\2\2\2\16_\3\2\2\2\20d\3\2\2\2\22o\3\2\2\2\24}\3\2")
        buf.write("\2\2\26\177\3\2\2\2\30\u0088\3\2\2\2\32\u0096\3\2\2\2")
        buf.write("\34\u009e\3\2\2\2\36\u00a9\3\2\2\2 \u00b6\3\2\2\2\"\u00df")
        buf.write("\3\2\2\2$\u0104\3\2\2\2&\u010c\3\2\2\2(\u010e\3\2\2\2")
        buf.write("*\u0112\3\2\2\2,\u0115\3\2\2\2.\u0122\3\2\2\2\60\u0124")
        buf.write("\3\2\2\2\62\u012c\3\2\2\2\64\u012f\3\2\2\2\66\u0132\3")
        buf.write("\2\2\28\u014b\3\2\2\2:\u014d\3\2\2\2<\u0150\3\2\2\2>@")
        buf.write("\5\4\3\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2BC\3\2")
        buf.write("\2\2CD\7\2\2\3D\3\3\2\2\2EG\7\23\2\2FH\5\6\4\2GF\3\2\2")
        buf.write("\2GH\3\2\2\2HI\3\2\2\2IJ\7;\2\2JK\7\63\2\2KL\5\b\5\2L")
        buf.write("M\7\64\2\2M\5\3\2\2\2NO\7;\2\2OP\7\3\2\2P\7\3\2\2\2QS")
        buf.write("\5\n\6\2RQ\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2U\t\3")
        buf.write("\2\2\2VT\3\2\2\2W[\5\f\7\2X[\5\30\r\2Y[\5\26\f\2ZW\3\2")
        buf.write("\2\2ZX\3\2\2\2ZY\3\2\2\2[\13\3\2\2\2\\]\5\16\b\2]^\7\65")
        buf.write("\2\2^\r\3\2\2\2_b\t\2\2\2`c\5\22\n\2ac\5\20\t\2b`\3\2")
        buf.write("\2\2ba\3\2\2\2c\17\3\2\2\2di\t\3\2\2ef\7\62\2\2fh\t\3")
        buf.write("\2\2ge\3\2\2\2hk\3\2\2\2ig\3\2\2\2ij\3\2\2\2jl\3\2\2\2")
        buf.write("ki\3\2\2\2lm\7\66\2\2mn\5 \21\2n\21\3\2\2\2op\t\3\2\2")
        buf.write("pq\5\24\13\2qr\5\"\22\2r\23\3\2\2\2st\7\62\2\2tu\t\3\2")
        buf.write("\2uv\5\24\13\2vw\5\"\22\2wx\7\62\2\2x~\3\2\2\2yz\7\66")
        buf.write("\2\2z{\5 \21\2{|\7&\2\2|~\3\2\2\2}s\3\2\2\2}y\3\2\2\2")
        buf.write("~\25\3\2\2\2\177\u0080\7\32\2\2\u0080\u0081\7\24\2\2\u0081")
        buf.write("\u0083\7-\2\2\u0082\u0084\5\32\16\2\u0083\u0082\3\2\2")
        buf.write("\2\u0083\u0084\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0086")
        buf.write("\7.\2\2\u0086\u0087\5<\37\2\u0087\27\3\2\2\2\u0088\u0089")
        buf.write("\7\32\2\2\u0089\u008a\t\3\2\2\u008a\u008c\7-\2\2\u008b")
        buf.write("\u008d\5\32\16\2\u008c\u008b\3\2\2\2\u008c\u008d\3\2\2")
        buf.write("\2\u008d\u008e\3\2\2\2\u008e\u008f\7.\2\2\u008f\u0092")
        buf.write("\7\66\2\2\u0090\u0093\5 \21\2\u0091\u0093\7\30\2\2\u0092")
        buf.write("\u0090\3\2\2\2\u0092\u0091\3\2\2\2\u0093\u0094\3\2\2\2")
        buf.write("\u0094\u0095\5<\37\2\u0095\31\3\2\2\2\u0096\u009b\5\34")
        buf.write("\17\2\u0097\u0098\7\62\2\2\u0098\u009a\5\34\17\2\u0099")
        buf.write("\u0097\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2")
        buf.write("\u009b\u009c\3\2\2\2\u009c\33\3\2\2\2\u009d\u009b\3\2")
        buf.write("\2\2\u009e\u00a3\7;\2\2\u009f\u00a0\7\62\2\2\u00a0\u00a2")
        buf.write("\7;\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3")
        buf.write("\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a6\3\2\2\2")
        buf.write("\u00a5\u00a3\3\2\2\2\u00a6\u00a7\7\66\2\2\u00a7\u00a8")
        buf.write("\5 \21\2\u00a8\35\3\2\2\2\u00a9\u00ab\7/\2\2\u00aa\u00ac")
        buf.write("\t\4\2\2\u00ab\u00aa\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac")
        buf.write("\u00b1\3\2\2\2\u00ad\u00ae\7\62\2\2\u00ae\u00b0\t\4\2")
        buf.write("\2\u00af\u00ad\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af")
        buf.write("\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b4\3\2\2\2\u00b3")
        buf.write("\u00b1\3\2\2\2\u00b4\u00b5\7\60\2\2\u00b5\37\3\2\2\2\u00b6")
        buf.write("\u00b7\t\5\2\2\u00b7!\3\2\2\2\u00b8\u00b9\b\22\1\2\u00b9")
        buf.write("\u00ba\7-\2\2\u00ba\u00bb\5\"\22\2\u00bb\u00bc\7.\2\2")
        buf.write("\u00bc\u00e0\3\2\2\2\u00bd\u00be\7\27\2\2\u00be\u00bf")
        buf.write("\7;\2\2\u00bf\u00c1\7-\2\2\u00c0\u00c2\5$\23\2\u00c1\u00c0")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3")
        buf.write("\u00e0\7.\2\2\u00c4\u00c5\7;\2\2\u00c5\u00c7\7\61\2\2")
        buf.write("\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\3")
        buf.write("\2\2\2\u00c8\u00ce\7<\2\2\u00c9\u00cb\7-\2\2\u00ca\u00cc")
        buf.write("\5$\23\2\u00cb\u00ca\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc")
        buf.write("\u00cd\3\2\2\2\u00cd\u00cf\7.\2\2\u00ce\u00c9\3\2\2\2")
        buf.write("\u00ce\u00cf\3\2\2\2\u00cf\u00e0\3\2\2\2\u00d0\u00d1\7")
        buf.write("\34\2\2\u00d1\u00e0\5\"\22\f\u00d2\u00d3\7!\2\2\u00d3")
        buf.write("\u00e0\5\"\22\13\u00d4\u00dc\78\2\2\u00d5\u00dc\7\67\2")
        buf.write("\2\u00d6\u00dc\7\13\2\2\u00d7\u00dc\7\f\2\2\u00d8\u00dc")
        buf.write("\79\2\2\u00d9\u00dc\5\36\20\2\u00da\u00dc\7\22\2\2\u00db")
        buf.write("\u00d4\3\2\2\2\u00db\u00d5\3\2\2\2\u00db\u00d6\3\2\2\2")
        buf.write("\u00db\u00d7\3\2\2\2\u00db\u00d8\3\2\2\2\u00db\u00d9\3")
        buf.write("\2\2\2\u00db\u00da\3\2\2\2\u00dc\u00e0\3\2\2\2\u00dd\u00e0")
        buf.write("\7\26\2\2\u00de\u00e0\7;\2\2\u00df\u00b8\3\2\2\2\u00df")
        buf.write("\u00bd\3\2\2\2\u00df\u00c6\3\2\2\2\u00df\u00d0\3\2\2\2")
        buf.write("\u00df\u00d2\3\2\2\2\u00df\u00db\3\2\2\2\u00df\u00dd\3")
        buf.write("\2\2\2\u00df\u00de\3\2\2\2\u00e0\u0101\3\2\2\2\u00e1\u00e2")
        buf.write("\f\n\2\2\u00e2\u00e3\t\6\2\2\u00e3\u0100\5\"\22\13\u00e4")
        buf.write("\u00e5\f\t\2\2\u00e5\u00e6\t\7\2\2\u00e6\u0100\5\"\22")
        buf.write("\n\u00e7\u00e8\f\b\2\2\u00e8\u00e9\t\b\2\2\u00e9\u0100")
        buf.write("\5\"\22\t\u00ea\u00eb\f\7\2\2\u00eb\u00ec\t\t\2\2\u00ec")
        buf.write("\u0100\5\"\22\b\u00ed\u00ee\f\6\2\2\u00ee\u00ef\7+\2\2")
        buf.write("\u00ef\u0100\5\"\22\7\u00f0\u00f1\f\16\2\2\u00f1\u00f2")
        buf.write("\7\61\2\2\u00f2\u00f8\7;\2\2\u00f3\u00f5\7-\2\2\u00f4")
        buf.write("\u00f6\5$\23\2\u00f5\u00f4\3\2\2\2\u00f5\u00f6\3\2\2\2")
        buf.write("\u00f6\u00f7\3\2\2\2\u00f7\u00f9\7.\2\2\u00f8\u00f3\3")
        buf.write("\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u0100\3\2\2\2\u00fa\u00fb")
        buf.write("\f\r\2\2\u00fb\u00fc\7/\2\2\u00fc\u00fd\5\"\22\2\u00fd")
        buf.write("\u00fe\7\60\2\2\u00fe\u0100\3\2\2\2\u00ff\u00e1\3\2\2")
        buf.write("\2\u00ff\u00e4\3\2\2\2\u00ff\u00e7\3\2\2\2\u00ff\u00ea")
        buf.write("\3\2\2\2\u00ff\u00ed\3\2\2\2\u00ff\u00f0\3\2\2\2\u00ff")
        buf.write("\u00fa\3\2\2\2\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2")
        buf.write("\u0101\u0102\3\2\2\2\u0102#\3\2\2\2\u0103\u0101\3\2\2")
        buf.write("\2\u0104\u0109\5\"\22\2\u0105\u0106\7\62\2\2\u0106\u0108")
        buf.write("\5\"\22\2\u0107\u0105\3\2\2\2\u0108\u010b\3\2\2\2\u0109")
        buf.write("\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a%\3\2\2\2\u010b")
        buf.write("\u0109\3\2\2\2\u010c\u010d\5\f\7\2\u010d\'\3\2\2\2\u010e")
        buf.write("\u010f\5\"\22\2\u010f\u0110\7%\2\2\u0110\u0111\5\"\22")
        buf.write("\2\u0111)\3\2\2\2\u0112\u0113\5(\25\2\u0113\u0114\7\65")
        buf.write("\2\2\u0114+\3\2\2\2\u0115\u0117\7\b\2\2\u0116\u0118\5")
        buf.write("<\37\2\u0117\u0116\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0119")
        buf.write("\3\2\2\2\u0119\u011a\5\"\22\2\u011a\u011d\5<\37\2\u011b")
        buf.write("\u011c\7\t\2\2\u011c\u011e\5<\37\2\u011d\u011b\3\2\2\2")
        buf.write("\u011d\u011e\3\2\2\2\u011e-\3\2\2\2\u011f\u0123\5(\25")
        buf.write("\2\u0120\u0123\58\35\2\u0121\u0123\5\16\b\2\u0122\u011f")
        buf.write("\3\2\2\2\u0122\u0120\3\2\2\2\u0122\u0121\3\2\2\2\u0123")
        buf.write("/\3\2\2\2\u0124\u0125\7\n\2\2\u0125\u0126\5.\30\2\u0126")
        buf.write("\u0127\7\65\2\2\u0127\u0128\5\"\22\2\u0128\u0129\7\65")
        buf.write("\2\2\u0129\u012a\5.\30\2\u012a\u012b\5<\37\2\u012b\61")
        buf.write("\3\2\2\2\u012c\u012d\7\6\2\2\u012d\u012e\7\65\2\2\u012e")
        buf.write("\63\3\2\2\2\u012f\u0130\7\7\2\2\u0130\u0131\7\65\2\2\u0131")
        buf.write("\65\3\2\2\2\u0132\u0134\7\21\2\2\u0133\u0135\5\"\22\2")
        buf.write("\u0134\u0133\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\3")
        buf.write("\2\2\2\u0136\u0137\7\65\2\2\u0137\67\3\2\2\2\u0138\u0139")
        buf.write("\5\"\22\2\u0139\u013a\7\61\2\2\u013a\u013b\7;\2\2\u013b")
        buf.write("\u013d\7-\2\2\u013c\u013e\5$\23\2\u013d\u013c\3\2\2\2")
        buf.write("\u013d\u013e\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140\7")
        buf.write(".\2\2\u0140\u014c\3\2\2\2\u0141\u0142\7;\2\2\u0142\u0144")
        buf.write("\7\61\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144")
        buf.write("\u0145\3\2\2\2\u0145\u0146\7<\2\2\u0146\u0148\7-\2\2\u0147")
        buf.write("\u0149\5$\23\2\u0148\u0147\3\2\2\2\u0148\u0149\3\2\2\2")
        buf.write("\u0149\u014a\3\2\2\2\u014a\u014c\7.\2\2\u014b\u0138\3")
        buf.write("\2\2\2\u014b\u0143\3\2\2\2\u014c9\3\2\2\2\u014d\u014e")
        buf.write("\58\35\2\u014e\u014f\7\65\2\2\u014f;\3\2\2\2\u0150\u015b")
        buf.write("\7\63\2\2\u0151\u015a\5&\24\2\u0152\u015a\5*\26\2\u0153")
        buf.write("\u015a\5,\27\2\u0154\u015a\5\60\31\2\u0155\u015a\5\62")
        buf.write("\32\2\u0156\u015a\5\64\33\2\u0157\u015a\5\66\34\2\u0158")
        buf.write("\u015a\5:\36\2\u0159\u0151\3\2\2\2\u0159\u0152\3\2\2\2")
        buf.write("\u0159\u0153\3\2\2\2\u0159\u0154\3\2\2\2\u0159\u0155\3")
        buf.write("\2\2\2\u0159\u0156\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u0158")
        buf.write("\3\2\2\2\u015a\u015d\3\2\2\2\u015b\u0159\3\2\2\2\u015b")
        buf.write("\u015c\3\2\2\2\u015c\u015e\3\2\2\2\u015d\u015b\3\2\2\2")
        buf.write("\u015e\u015f\7\64\2\2\u015f=\3\2\2\2%AGTZbi}\u0083\u008c")
        buf.write("\u0092\u009b\u00a3\u00ab\u00b1\u00c1\u00c6\u00cb\u00ce")
        buf.write("\u00db\u00df\u00f5\u00f8\u00ff\u0101\u0109\u0117\u011d")
        buf.write("\u0122\u0134\u013d\u0143\u0148\u014b\u0159\u015b")
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
                     "'-'", "'*'", "'/'", "'\\'", "'!='", "'!'", "'&&'", 
                     "'||'", "'=='", "':='", "'='", "'<='", "'<'", "'>='", 
                     "'>'", "'^'", "'%'", "'('", "')'", "'['", "']'", "'.'", 
                     "','", "'{'", "'}'", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", 
                      "FALSE", "INT", "FLOAT", "BOOL", "STRING", "RETURN", 
                      "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", 
                      "VOID", "CONST", "FUNC", "ADD_OP", "SUB_OP", "MUL_OP", 
                      "DIV_OP", "BACKSLASH", "NOT_EQUAL", "NEGATE", "AND", 
                      "OR", "EQUAL", "DECLARE_ASSIGN_OP", "ASSIGN_OP", "LESS_EQUAL", 
                      "LESS_THAN", "GREATER_EQUAL", "GREATER_THAN", "POW_OP", 
                      "MOD_OP", "LB", "RB", "LS", "RS", "DOT", "CM", "LP", 
                      "RP", "SEMI", "COLON", "FLOAT_LIT", "INT_LIT", "STRING_LIT", 
                      "ARRAY_TYPE", "ID", "AT_ID", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_dcl = 1
    RULE_class_super = 2
    RULE_class_body = 3
    RULE_class_member = 4
    RULE_attribute_decl = 5
    RULE_attribute_decl_body = 6
    RULE_attribute_decl_inner_without_init = 7
    RULE_attribute_decl_inner_with_init = 8
    RULE_attribute_decl_inner_with_init_tail = 9
    RULE_constructor_method = 10
    RULE_method = 11
    RULE_param_list = 12
    RULE_param = 13
    RULE_array_lit = 14
    RULE_data_type = 15
    RULE_expr = 16
    RULE_expr_list = 17
    RULE_dcl_stmt = 18
    RULE_assign_stmt_body = 19
    RULE_assign_stmt = 20
    RULE_if_stmt = 21
    RULE_for_stmt_inner = 22
    RULE_for_stmt = 23
    RULE_break_stmt = 24
    RULE_continue_stmt = 25
    RULE_return_stmt = 26
    RULE_method_invocation_stmt_body = 27
    RULE_method_invocation_stmt = 28
    RULE_block_stmt = 29

    ruleNames =  [ "program", "class_dcl", "class_super", "class_body", 
                   "class_member", "attribute_decl", "attribute_decl_body", 
                   "attribute_decl_inner_without_init", "attribute_decl_inner_with_init", 
                   "attribute_decl_inner_with_init_tail", "constructor_method", 
                   "method", "param_list", "param", "array_lit", "data_type", 
                   "expr", "expr_list", "dcl_stmt", "assign_stmt_body", 
                   "assign_stmt", "if_stmt", "for_stmt_inner", "for_stmt", 
                   "break_stmt", "continue_stmt", "return_stmt", "method_invocation_stmt_body", 
                   "method_invocation_stmt", "block_stmt" ]

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
    NOT_EQUAL=30
    NEGATE=31
    AND=32
    OR=33
    EQUAL=34
    DECLARE_ASSIGN_OP=35
    ASSIGN_OP=36
    LESS_EQUAL=37
    LESS_THAN=38
    GREATER_EQUAL=39
    GREATER_THAN=40
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
    FLOAT_LIT=53
    INT_LIT=54
    STRING_LIT=55
    ARRAY_TYPE=56
    ID=57
    AT_ID=58
    WS=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61
    ERROR_CHAR=62

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




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.class_dcl()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSlangParser.CLASS):
                    break

            self.state = 65
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




    def class_dcl(self):

        localctx = CSlangParser.Class_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_dcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(CSlangParser.CLASS)
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 68
                self.class_super()


            self.state = 71
            self.match(CSlangParser.ID)
            self.state = 72
            self.match(CSlangParser.LP)
            self.state = 73
            self.class_body()
            self.state = 74
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




    def class_super(self):

        localctx = CSlangParser.Class_superContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_super)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(CSlangParser.ID)
            self.state = 77
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




    def class_body(self):

        localctx = CSlangParser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.VAR) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC))) != 0):
                self.state = 79
                self.class_member()
                self.state = 84
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

        def attribute_decl(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_declContext,0)


        def method(self):
            return self.getTypedRuleContext(CSlangParser.MethodContext,0)


        def constructor_method(self):
            return self.getTypedRuleContext(CSlangParser.Constructor_methodContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_member




    def class_member(self):

        localctx = CSlangParser.Class_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_member)
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.attribute_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.method()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.constructor_method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_decl_body(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_decl_bodyContext,0)


        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attribute_decl




    def attribute_decl(self):

        localctx = CSlangParser.Attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.attribute_decl_body()
            self.state = 91
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_decl_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def attribute_decl_inner_with_init(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_decl_inner_with_initContext,0)


        def attribute_decl_inner_without_init(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_decl_inner_without_initContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attribute_decl_body




    def attribute_decl_body(self):

        localctx = CSlangParser.Attribute_decl_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute_decl_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 94
                self.attribute_decl_inner_with_init()
                pass

            elif la_ == 2:
                self.state = 95
                self.attribute_decl_inner_without_init()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_decl_inner_without_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(CSlangParser.Data_typeContext,0)


        def AT_ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.AT_ID)
            else:
                return self.getToken(CSlangParser.AT_ID, i)

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

        def getRuleIndex(self):
            return CSlangParser.RULE_attribute_decl_inner_without_init




    def attribute_decl_inner_without_init(self):

        localctx = CSlangParser.Attribute_decl_inner_without_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attribute_decl_inner_without_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 99
                self.match(CSlangParser.CM)
                self.state = 100
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(CSlangParser.COLON)
            self.state = 107
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_decl_inner_with_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_decl_inner_with_init_tail(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_decl_inner_with_init_tailContext,0)


        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attribute_decl_inner_with_init




    def attribute_decl_inner_with_init(self):

        localctx = CSlangParser.Attribute_decl_inner_with_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attribute_decl_inner_with_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 110
            self.attribute_decl_inner_with_init_tail()
            self.state = 111
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_decl_inner_with_init_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def attribute_decl_inner_with_init_tail(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_decl_inner_with_init_tailContext,0)


        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(CSlangParser.Data_typeContext,0)


        def ASSIGN_OP(self):
            return self.getToken(CSlangParser.ASSIGN_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attribute_decl_inner_with_init_tail




    def attribute_decl_inner_with_init_tail(self):

        localctx = CSlangParser.Attribute_decl_inner_with_init_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attribute_decl_inner_with_init_tail)
        self._la = 0 # Token type
        try:
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(CSlangParser.CM)
                self.state = 114
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 115
                self.attribute_decl_inner_with_init_tail()
                self.state = 116
                self.expr(0)
                self.state = 117
                self.match(CSlangParser.CM)
                pass
            elif token in [CSlangParser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(CSlangParser.COLON)
                self.state = 120
                self.data_type()
                self.state = 121
                self.match(CSlangParser.ASSIGN_OP)
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


    class Constructor_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def CONSTRUCTOR(self):
            return self.getToken(CSlangParser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def param_list(self):
            return self.getTypedRuleContext(CSlangParser.Param_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constructor_method




    def constructor_method(self):

        localctx = CSlangParser.Constructor_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_constructor_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(CSlangParser.FUNC)
            self.state = 126
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 127
            self.match(CSlangParser.LB)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 128
                self.param_list()


            self.state = 131
            self.match(CSlangParser.RB)
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

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def data_type(self):
            return self.getTypedRuleContext(CSlangParser.Data_typeContext,0)


        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def param_list(self):
            return self.getTypedRuleContext(CSlangParser.Param_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_method




    def method(self):

        localctx = CSlangParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(CSlangParser.FUNC)
            self.state = 135
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 136
            self.match(CSlangParser.LB)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 137
                self.param_list()


            self.state = 140
            self.match(CSlangParser.RB)
            self.state = 141
            self.match(CSlangParser.COLON)
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.ARRAY_TYPE, CSlangParser.ID]:
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




    def param_list(self):

        localctx = CSlangParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param_list)
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




    def param(self):

        localctx = CSlangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param)
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


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(CSlangParser.LS, 0)

        def RS(self):
            return self.getToken(CSlangParser.RS, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.INT_LIT)
            else:
                return self.getToken(CSlangParser.INT_LIT, i)

        def FLOAT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.FLOAT_LIT)
            else:
                return self.getToken(CSlangParser.FLOAT_LIT, i)

        def TRUE(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.TRUE)
            else:
                return self.getToken(CSlangParser.TRUE, i)

        def FALSE(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.FALSE)
            else:
                return self.getToken(CSlangParser.FALSE, i)

        def STRING_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.STRING_LIT)
            else:
                return self.getToken(CSlangParser.STRING_LIT, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_array_lit




    def array_lit(self):

        localctx = CSlangParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(CSlangParser.LS)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STRING_LIT))) != 0):
                self.state = 168
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STRING_LIT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 171
                self.match(CSlangParser.CM)
                self.state = 172
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STRING_LIT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 178
            self.match(CSlangParser.RS)
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

        def ARRAY_TYPE(self):
            return self.getToken(CSlangParser.ARRAY_TYPE, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_data_type




    def data_type(self):

        localctx = CSlangParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.INT) | (1 << CSlangParser.FLOAT) | (1 << CSlangParser.BOOL) | (1 << CSlangParser.STRING) | (1 << CSlangParser.ARRAY_TYPE) | (1 << CSlangParser.ID))) != 0)):
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprContext,i)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def expr_list(self):
            return self.getTypedRuleContext(CSlangParser.Expr_listContext,0)


        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def SUB_OP(self):
            return self.getToken(CSlangParser.SUB_OP, 0)

        def NEGATE(self):
            return self.getToken(CSlangParser.NEGATE, 0)

        def INT_LIT(self):
            return self.getToken(CSlangParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(CSlangParser.FLOAT_LIT, 0)

        def TRUE(self):
            return self.getToken(CSlangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CSlangParser.FALSE, 0)

        def STRING_LIT(self):
            return self.getToken(CSlangParser.STRING_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(CSlangParser.Array_litContext,0)


        def NULL(self):
            return self.getToken(CSlangParser.NULL, 0)

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def MUL_OP(self):
            return self.getToken(CSlangParser.MUL_OP, 0)

        def DIV_OP(self):
            return self.getToken(CSlangParser.DIV_OP, 0)

        def BACKSLASH(self):
            return self.getToken(CSlangParser.BACKSLASH, 0)

        def MOD_OP(self):
            return self.getToken(CSlangParser.MOD_OP, 0)

        def ADD_OP(self):
            return self.getToken(CSlangParser.ADD_OP, 0)

        def AND(self):
            return self.getToken(CSlangParser.AND, 0)

        def OR(self):
            return self.getToken(CSlangParser.OR, 0)

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

        def POW_OP(self):
            return self.getToken(CSlangParser.POW_OP, 0)

        def LS(self):
            return self.getToken(CSlangParser.LS, 0)

        def RS(self):
            return self.getToken(CSlangParser.RS, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 183
                self.match(CSlangParser.LB)
                self.state = 184
                self.expr(0)
                self.state = 185
                self.match(CSlangParser.RB)
                pass

            elif la_ == 2:
                self.state = 187
                self.match(CSlangParser.NEW)
                self.state = 188
                self.match(CSlangParser.ID)
                self.state = 189
                self.match(CSlangParser.LB)
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NEGATE) | (1 << CSlangParser.LB) | (1 << CSlangParser.LS) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STRING_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                    self.state = 190
                    self.expr_list()


                self.state = 193
                self.match(CSlangParser.RB)
                pass

            elif la_ == 3:
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 194
                    self.match(CSlangParser.ID)
                    self.state = 195
                    self.match(CSlangParser.DOT)


                self.state = 198
                self.match(CSlangParser.AT_ID)
                self.state = 204
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 199
                    self.match(CSlangParser.LB)
                    self.state = 201
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NEGATE) | (1 << CSlangParser.LB) | (1 << CSlangParser.LS) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STRING_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                        self.state = 200
                        self.expr_list()


                    self.state = 203
                    self.match(CSlangParser.RB)


                pass

            elif la_ == 4:
                self.state = 206
                self.match(CSlangParser.SUB_OP)
                self.state = 207
                self.expr(10)
                pass

            elif la_ == 5:
                self.state = 208
                self.match(CSlangParser.NEGATE)
                self.state = 209
                self.expr(9)
                pass

            elif la_ == 6:
                self.state = 217
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.INT_LIT]:
                    self.state = 210
                    self.match(CSlangParser.INT_LIT)
                    pass
                elif token in [CSlangParser.FLOAT_LIT]:
                    self.state = 211
                    self.match(CSlangParser.FLOAT_LIT)
                    pass
                elif token in [CSlangParser.TRUE]:
                    self.state = 212
                    self.match(CSlangParser.TRUE)
                    pass
                elif token in [CSlangParser.FALSE]:
                    self.state = 213
                    self.match(CSlangParser.FALSE)
                    pass
                elif token in [CSlangParser.STRING_LIT]:
                    self.state = 214
                    self.match(CSlangParser.STRING_LIT)
                    pass
                elif token in [CSlangParser.LS]:
                    self.state = 215
                    self.array_lit()
                    pass
                elif token in [CSlangParser.NULL]:
                    self.state = 216
                    self.match(CSlangParser.NULL)
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 7:
                self.state = 219
                self.match(CSlangParser.SELF)
                pass

            elif la_ == 8:
                self.state = 220
                self.match(CSlangParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 255
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 253
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 223
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 224
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MUL_OP) | (1 << CSlangParser.DIV_OP) | (1 << CSlangParser.BACKSLASH) | (1 << CSlangParser.MOD_OP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 225
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 226
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 227
                        _la = self._input.LA(1)
                        if not(_la==CSlangParser.ADD_OP or _la==CSlangParser.SUB_OP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 228
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = CSlangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 229
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 230
                        _la = self._input.LA(1)
                        if not(_la==CSlangParser.AND or _la==CSlangParser.OR):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 231
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = CSlangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 232
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 233
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.NOT_EQUAL) | (1 << CSlangParser.EQUAL) | (1 << CSlangParser.LESS_EQUAL) | (1 << CSlangParser.LESS_THAN) | (1 << CSlangParser.GREATER_EQUAL) | (1 << CSlangParser.GREATER_THAN))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 234
                        self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = CSlangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 235
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 236
                        self.match(CSlangParser.POW_OP)
                        self.state = 237
                        self.expr(5)
                        pass

                    elif la_ == 6:
                        localctx = CSlangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 238
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 239
                        self.match(CSlangParser.DOT)
                        self.state = 240
                        self.match(CSlangParser.ID)
                        self.state = 246
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                        if la_ == 1:
                            self.state = 241
                            self.match(CSlangParser.LB)
                            self.state = 243
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NEGATE) | (1 << CSlangParser.LB) | (1 << CSlangParser.LS) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STRING_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                                self.state = 242
                                self.expr_list()


                            self.state = 245
                            self.match(CSlangParser.RB)


                        pass

                    elif la_ == 7:
                        localctx = CSlangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 248
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 249
                        self.match(CSlangParser.LS)
                        self.state = 250
                        self.expr(0)
                        self.state = 251
                        self.match(CSlangParser.RS)
                        pass

             
                self.state = 257
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr_list




    def expr_list(self):

        localctx = CSlangParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.expr(0)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 259
                self.match(CSlangParser.CM)
                self.state = 260
                self.expr(0)
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def attribute_decl(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_dcl_stmt




    def dcl_stmt(self):

        localctx = CSlangParser.Dcl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_dcl_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.attribute_decl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmt_bodyContext(ParserRuleContext):
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

        def getRuleIndex(self):
            return CSlangParser.RULE_assign_stmt_body




    def assign_stmt_body(self):

        localctx = CSlangParser.Assign_stmt_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assign_stmt_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.expr(0)
            self.state = 269
            self.match(CSlangParser.DECLARE_ASSIGN_OP)
            self.state = 270
            self.expr(0)
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

        def assign_stmt_body(self):
            return self.getTypedRuleContext(CSlangParser.Assign_stmt_bodyContext,0)


        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = CSlangParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.assign_stmt_body()
            self.state = 273
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




    def if_stmt(self):

        localctx = CSlangParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(CSlangParser.IF)
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LP:
                self.state = 276
                self.block_stmt()


            self.state = 279
            self.expr(0)
            self.state = 280
            self.block_stmt()
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 281
                self.match(CSlangParser.ELSE)
                self.state = 282
                self.block_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmt_innerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt_body(self):
            return self.getTypedRuleContext(CSlangParser.Assign_stmt_bodyContext,0)


        def method_invocation_stmt_body(self):
            return self.getTypedRuleContext(CSlangParser.Method_invocation_stmt_bodyContext,0)


        def attribute_decl_body(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_decl_bodyContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_for_stmt_inner




    def for_stmt_inner(self):

        localctx = CSlangParser.For_stmt_innerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_for_stmt_inner)
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.assign_stmt_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.method_invocation_stmt_body()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 287
                self.attribute_decl_body()
                pass


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

        def for_stmt_inner(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.For_stmt_innerContext)
            else:
                return self.getTypedRuleContext(CSlangParser.For_stmt_innerContext,i)


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




    def for_stmt(self):

        localctx = CSlangParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(CSlangParser.FOR)
            self.state = 291
            self.for_stmt_inner()
            self.state = 292
            self.match(CSlangParser.SEMI)
            self.state = 293
            self.expr(0)
            self.state = 294
            self.match(CSlangParser.SEMI)
            self.state = 295
            self.for_stmt_inner()
            self.state = 296
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




    def break_stmt(self):

        localctx = CSlangParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(CSlangParser.BREAK)
            self.state = 299
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




    def continue_stmt(self):

        localctx = CSlangParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(CSlangParser.CONTINUE)
            self.state = 302
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




    def return_stmt(self):

        localctx = CSlangParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(CSlangParser.RETURN)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NEGATE) | (1 << CSlangParser.LB) | (1 << CSlangParser.LS) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STRING_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 305
                self.expr(0)


            self.state = 308
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocation_stmt_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(CSlangParser.Expr_listContext,0)


        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_method_invocation_stmt_body




    def method_invocation_stmt_body(self):

        localctx = CSlangParser.Method_invocation_stmt_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_method_invocation_stmt_body)
        self._la = 0 # Token type
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.expr(0)
                self.state = 311
                self.match(CSlangParser.DOT)
                self.state = 312
                self.match(CSlangParser.ID)
                self.state = 313
                self.match(CSlangParser.LB)
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NEGATE) | (1 << CSlangParser.LB) | (1 << CSlangParser.LS) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STRING_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                    self.state = 314
                    self.expr_list()


                self.state = 317
                self.match(CSlangParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 319
                    self.match(CSlangParser.ID)
                    self.state = 320
                    self.match(CSlangParser.DOT)


                self.state = 323
                self.match(CSlangParser.AT_ID)
                self.state = 324
                self.match(CSlangParser.LB)
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NEGATE) | (1 << CSlangParser.LB) | (1 << CSlangParser.LS) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STRING_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                    self.state = 325
                    self.expr_list()


                self.state = 328
                self.match(CSlangParser.RB)
                pass


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

        def method_invocation_stmt_body(self):
            return self.getTypedRuleContext(CSlangParser.Method_invocation_stmt_bodyContext,0)


        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_method_invocation_stmt




    def method_invocation_stmt(self):

        localctx = CSlangParser.Method_invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_method_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.method_invocation_stmt_body()
            self.state = 332
            self.match(CSlangParser.SEMI)
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

        def dcl_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Dcl_stmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Dcl_stmtContext,i)


        def assign_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Assign_stmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Assign_stmtContext,i)


        def if_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.If_stmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.If_stmtContext,i)


        def for_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.For_stmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.For_stmtContext,i)


        def break_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Break_stmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Break_stmtContext,i)


        def continue_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Continue_stmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Continue_stmtContext,i)


        def return_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Return_stmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Return_stmtContext,i)


        def method_invocation_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Method_invocation_stmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Method_invocation_stmtContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_block_stmt




    def block_stmt(self):

        localctx = CSlangParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(CSlangParser.LP)
            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.NULL) | (1 << CSlangParser.VAR) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.CONST) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NEGATE) | (1 << CSlangParser.LB) | (1 << CSlangParser.LS) | (1 << CSlangParser.FLOAT_LIT) | (1 << CSlangParser.INT_LIT) | (1 << CSlangParser.STRING_LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 343
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                if la_ == 1:
                    self.state = 335
                    self.dcl_stmt()
                    pass

                elif la_ == 2:
                    self.state = 336
                    self.assign_stmt()
                    pass

                elif la_ == 3:
                    self.state = 337
                    self.if_stmt()
                    pass

                elif la_ == 4:
                    self.state = 338
                    self.for_stmt()
                    pass

                elif la_ == 5:
                    self.state = 339
                    self.break_stmt()
                    pass

                elif la_ == 6:
                    self.state = 340
                    self.continue_stmt()
                    pass

                elif la_ == 7:
                    self.state = 341
                    self.return_stmt()
                    pass

                elif la_ == 8:
                    self.state = 342
                    self.method_invocation_stmt()
                    pass


                self.state = 347
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 348
            self.match(CSlangParser.RP)
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
        self._predicates[16] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 11)
         




