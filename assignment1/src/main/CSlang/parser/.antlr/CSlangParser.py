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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u0149\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2\6\2")
        buf.write("<\n\2\r\2\16\2=\3\2\3\2\3\3\3\3\5\3D\n\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\5\7\5O\n\5\f\5\16\5R\13\5\3\6\3\6")
        buf.write("\5\6V\n\6\3\7\3\7\3\7\5\7[\n\7\3\7\3\7\3\b\3\b\3\b\7\b")
        buf.write("b\n\b\f\b\16\be\13\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nx\n\n\3\13\3\13")
        buf.write("\3\13\3\13\5\13~\n\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\5")
        buf.write("\f\u0087\n\f\3\f\3\f\3\f\3\f\5\f\u008d\n\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\7\r\u0094\n\r\f\r\16\r\u0097\13\r\3\16\3\16\3")
        buf.write("\16\7\16\u009c\n\16\f\16\16\16\u009f\13\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17")
        buf.write("\u00ad\n\17\3\17\3\17\3\17\5\17\u00b2\n\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\5\17\u00b9\n\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00c2\n\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00da\n\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\7\17\u00e1\n\17\f\17\16\17\u00e4\13")
        buf.write("\17\3\20\3\20\3\20\7\20\u00e9\n\20\f\20\16\20\u00ec\13")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00f7\n\21\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3")
        buf.write("\24\5\24\u0102\n\24\3\24\3\24\3\24\3\24\5\24\u0108\n\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\30\3\30\5\30\u011a\n\30\3\30\3\30\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31")
        buf.write("\u0128\n\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0130\n")
        buf.write("\31\3\32\3\32\7\32\u0134\n\32\f\32\16\32\u0137\13\32\3")
        buf.write("\32\3\32\3\33\3\33\3\33\3\33\3\33\5\33\u0140\n\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\2\3\34\36\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write("\2\t\4\2\25\25\31\31\3\2>?\4\2\35\37,,\3\2\33\34\3\2\"")
        buf.write("#\5\2  $$\'*\3\2\r\20\2\u015d\2;\3\2\2\2\4A\3\2\2\2\6")
        buf.write("J\3\2\2\2\bP\3\2\2\2\nU\3\2\2\2\fW\3\2\2\2\16^\3\2\2\2")
        buf.write("\20i\3\2\2\2\22w\3\2\2\2\24y\3\2\2\2\26\u0082\3\2\2\2")
        buf.write("\30\u0090\3\2\2\2\32\u0098\3\2\2\2\34\u00c1\3\2\2\2\36")
        buf.write("\u00e5\3\2\2\2 \u00f6\3\2\2\2\"\u00f8\3\2\2\2$\u00fa\3")
        buf.write("\2\2\2&\u00ff\3\2\2\2(\u0109\3\2\2\2*\u0111\3\2\2\2,\u0114")
        buf.write("\3\2\2\2.\u0117\3\2\2\2\60\u012f\3\2\2\2\62\u0131\3\2")
        buf.write("\2\2\64\u013f\3\2\2\2\66\u0141\3\2\2\28\u0146\3\2\2\2")
        buf.write(":<\5\4\3\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>?\3")
        buf.write("\2\2\2?@\7\2\2\3@\3\3\2\2\2AC\7\23\2\2BD\5\6\4\2CB\3\2")
        buf.write("\2\2CD\3\2\2\2DE\3\2\2\2EF\7>\2\2FG\7\63\2\2GH\5\b\5\2")
        buf.write("HI\7\64\2\2I\5\3\2\2\2JK\7>\2\2KL\7\3\2\2L\7\3\2\2\2M")
        buf.write("O\5\n\6\2NM\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\t\3")
        buf.write("\2\2\2RP\3\2\2\2SV\5\f\7\2TV\5\26\f\2US\3\2\2\2UT\3\2")
        buf.write("\2\2V\13\3\2\2\2WZ\t\2\2\2X[\5\20\t\2Y[\5\16\b\2ZX\3\2")
        buf.write("\2\2ZY\3\2\2\2[\\\3\2\2\2\\]\7\65\2\2]\r\3\2\2\2^c\t\3")
        buf.write("\2\2_`\7\62\2\2`b\t\3\2\2a_\3\2\2\2be\3\2\2\2ca\3\2\2")
        buf.write("\2cd\3\2\2\2df\3\2\2\2ec\3\2\2\2fg\7\66\2\2gh\5\64\33")
        buf.write("\2h\17\3\2\2\2ij\t\3\2\2jk\5\22\n\2kl\5\34\17\2l\21\3")
        buf.write("\2\2\2mn\7\62\2\2no\t\3\2\2op\5\22\n\2pq\5\34\17\2qr\7")
        buf.write("\62\2\2rx\3\2\2\2st\7\66\2\2tu\5\64\33\2uv\7&\2\2vx\3")
        buf.write("\2\2\2wm\3\2\2\2ws\3\2\2\2x\23\3\2\2\2yz\7\32\2\2z{\7")
        buf.write("\24\2\2{}\7-\2\2|~\5\30\r\2}|\3\2\2\2}~\3\2\2\2~\177\3")
        buf.write("\2\2\2\177\u0080\7.\2\2\u0080\u0081\5\62\32\2\u0081\25")
        buf.write("\3\2\2\2\u0082\u0083\7\32\2\2\u0083\u0084\t\3\2\2\u0084")
        buf.write("\u0086\7-\2\2\u0085\u0087\5\30\r\2\u0086\u0085\3\2\2\2")
        buf.write("\u0086\u0087\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\7")
        buf.write(".\2\2\u0089\u008c\7\66\2\2\u008a\u008d\5\64\33\2\u008b")
        buf.write("\u008d\7\30\2\2\u008c\u008a\3\2\2\2\u008c\u008b\3\2\2")
        buf.write("\2\u008d\u008e\3\2\2\2\u008e\u008f\5\62\32\2\u008f\27")
        buf.write("\3\2\2\2\u0090\u0095\5\32\16\2\u0091\u0092\7\62\2\2\u0092")
        buf.write("\u0094\5\32\16\2\u0093\u0091\3\2\2\2\u0094\u0097\3\2\2")
        buf.write("\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\31\3")
        buf.write("\2\2\2\u0097\u0095\3\2\2\2\u0098\u009d\7>\2\2\u0099\u009a")
        buf.write("\7\62\2\2\u009a\u009c\7>\2\2\u009b\u0099\3\2\2\2\u009c")
        buf.write("\u009f\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2")
        buf.write("\u009e\u00a0\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a1\7")
        buf.write("\66\2\2\u00a1\u00a2\5\64\33\2\u00a2\33\3\2\2\2\u00a3\u00a4")
        buf.write("\b\17\1\2\u00a4\u00a5\7-\2\2\u00a5\u00a6\5\34\17\2\u00a6")
        buf.write("\u00a7\7.\2\2\u00a7\u00c2\3\2\2\2\u00a8\u00a9\7\27\2\2")
        buf.write("\u00a9\u00aa\7>\2\2\u00aa\u00ac\7-\2\2\u00ab\u00ad\5\36")
        buf.write("\20\2\u00ac\u00ab\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae")
        buf.write("\3\2\2\2\u00ae\u00c2\7.\2\2\u00af\u00b0\7>\2\2\u00b0\u00b2")
        buf.write("\7\61\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2")
        buf.write("\u00b3\3\2\2\2\u00b3\u00b8\7?\2\2\u00b4\u00b5\7-\2\2\u00b5")
        buf.write("\u00b6\5\36\20\2\u00b6\u00b7\7.\2\2\u00b7\u00b9\3\2\2")
        buf.write("\2\u00b8\u00b4\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00c2")
        buf.write("\3\2\2\2\u00ba\u00bb\7\34\2\2\u00bb\u00c2\5\34\17\f\u00bc")
        buf.write("\u00bd\7!\2\2\u00bd\u00c2\5\34\17\13\u00be\u00c2\7\67")
        buf.write("\2\2\u00bf\u00c2\7\26\2\2\u00c0\u00c2\7>\2\2\u00c1\u00a3")
        buf.write("\3\2\2\2\u00c1\u00a8\3\2\2\2\u00c1\u00b1\3\2\2\2\u00c1")
        buf.write("\u00ba\3\2\2\2\u00c1\u00bc\3\2\2\2\u00c1\u00be\3\2\2\2")
        buf.write("\u00c1\u00bf\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\u00e2\3")
        buf.write("\2\2\2\u00c3\u00c4\f\n\2\2\u00c4\u00c5\t\4\2\2\u00c5\u00e1")
        buf.write("\5\34\17\13\u00c6\u00c7\f\t\2\2\u00c7\u00c8\t\5\2\2\u00c8")
        buf.write("\u00e1\5\34\17\n\u00c9\u00ca\f\b\2\2\u00ca\u00cb\t\6\2")
        buf.write("\2\u00cb\u00e1\5\34\17\t\u00cc\u00cd\f\7\2\2\u00cd\u00ce")
        buf.write("\t\7\2\2\u00ce\u00e1\5\34\17\b\u00cf\u00d0\f\6\2\2\u00d0")
        buf.write("\u00d1\7+\2\2\u00d1\u00e1\5\34\17\7\u00d2\u00d3\f\16\2")
        buf.write("\2\u00d3\u00d4\7\61\2\2\u00d4\u00d9\7>\2\2\u00d5\u00d6")
        buf.write("\7-\2\2\u00d6\u00d7\5\36\20\2\u00d7\u00d8\7.\2\2\u00d8")
        buf.write("\u00da\3\2\2\2\u00d9\u00d5\3\2\2\2\u00d9\u00da\3\2\2\2")
        buf.write("\u00da\u00e1\3\2\2\2\u00db\u00dc\f\r\2\2\u00dc\u00dd\7")
        buf.write("/\2\2\u00dd\u00de\5\34\17\2\u00de\u00df\7\60\2\2\u00df")
        buf.write("\u00e1\3\2\2\2\u00e0\u00c3\3\2\2\2\u00e0\u00c6\3\2\2\2")
        buf.write("\u00e0\u00c9\3\2\2\2\u00e0\u00cc\3\2\2\2\u00e0\u00cf\3")
        buf.write("\2\2\2\u00e0\u00d2\3\2\2\2\u00e0\u00db\3\2\2\2\u00e1\u00e4")
        buf.write("\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3")
        buf.write("\35\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00ea\5\34\17\2")
        buf.write("\u00e6\u00e7\7\62\2\2\u00e7\u00e9\5\34\17\2\u00e8\u00e6")
        buf.write("\3\2\2\2\u00e9\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea")
        buf.write("\u00eb\3\2\2\2\u00eb\37\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed")
        buf.write("\u00f7\5\"\22\2\u00ee\u00f7\5$\23\2\u00ef\u00f7\5&\24")
        buf.write("\2\u00f0\u00f7\5(\25\2\u00f1\u00f7\5*\26\2\u00f2\u00f7")
        buf.write("\5,\27\2\u00f3\u00f7\5.\30\2\u00f4\u00f7\5\60\31\2\u00f5")
        buf.write("\u00f7\5\62\32\2\u00f6\u00ed\3\2\2\2\u00f6\u00ee\3\2\2")
        buf.write("\2\u00f6\u00ef\3\2\2\2\u00f6\u00f0\3\2\2\2\u00f6\u00f1")
        buf.write("\3\2\2\2\u00f6\u00f2\3\2\2\2\u00f6\u00f3\3\2\2\2\u00f6")
        buf.write("\u00f4\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7!\3\2\2\2\u00f8")
        buf.write("\u00f9\5\f\7\2\u00f9#\3\2\2\2\u00fa\u00fb\5\34\17\2\u00fb")
        buf.write("\u00fc\7%\2\2\u00fc\u00fd\5\34\17\2\u00fd\u00fe\7\65\2")
        buf.write("\2\u00fe%\3\2\2\2\u00ff\u0101\7\b\2\2\u0100\u0102\5\62")
        buf.write("\32\2\u0101\u0100\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0103")
        buf.write("\3\2\2\2\u0103\u0104\5\34\17\2\u0104\u0107\5\62\32\2\u0105")
        buf.write("\u0106\7\t\2\2\u0106\u0108\5\62\32\2\u0107\u0105\3\2\2")
        buf.write("\2\u0107\u0108\3\2\2\2\u0108\'\3\2\2\2\u0109\u010a\7\n")
        buf.write("\2\2\u010a\u010b\5$\23\2\u010b\u010c\7\65\2\2\u010c\u010d")
        buf.write("\5\34\17\2\u010d\u010e\7\65\2\2\u010e\u010f\5$\23\2\u010f")
        buf.write("\u0110\5\62\32\2\u0110)\3\2\2\2\u0111\u0112\7\6\2\2\u0112")
        buf.write("\u0113\7\65\2\2\u0113+\3\2\2\2\u0114\u0115\7\7\2\2\u0115")
        buf.write("\u0116\7\65\2\2\u0116-\3\2\2\2\u0117\u0119\7\21\2\2\u0118")
        buf.write("\u011a\5\34\17\2\u0119\u0118\3\2\2\2\u0119\u011a\3\2\2")
        buf.write("\2\u011a\u011b\3\2\2\2\u011b\u011c\7\65\2\2\u011c/\3\2")
        buf.write("\2\2\u011d\u011e\5\34\17\2\u011e\u011f\7\61\2\2\u011f")
        buf.write("\u0120\7>\2\2\u0120\u0121\7-\2\2\u0121\u0122\5\36\20\2")
        buf.write("\u0122\u0123\7.\2\2\u0123\u0124\7\65\2\2\u0124\u0130\3")
        buf.write("\2\2\2\u0125\u0126\7>\2\2\u0126\u0128\7\61\2\2\u0127\u0125")
        buf.write("\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u0129\3\2\2\2\u0129")
        buf.write("\u012a\7?\2\2\u012a\u012b\7-\2\2\u012b\u012c\5\36\20\2")
        buf.write("\u012c\u012d\7.\2\2\u012d\u012e\7\65\2\2\u012e\u0130\3")
        buf.write("\2\2\2\u012f\u011d\3\2\2\2\u012f\u0127\3\2\2\2\u0130\61")
        buf.write("\3\2\2\2\u0131\u0135\7\63\2\2\u0132\u0134\5 \21\2\u0133")
        buf.write("\u0132\3\2\2\2\u0134\u0137\3\2\2\2\u0135\u0133\3\2\2\2")
        buf.write("\u0135\u0136\3\2\2\2\u0136\u0138\3\2\2\2\u0137\u0135\3")
        buf.write("\2\2\2\u0138\u0139\7\64\2\2\u0139\63\3\2\2\2\u013a\u0140")
        buf.write("\7\17\2\2\u013b\u0140\7\r\2\2\u013c\u0140\7\16\2\2\u013d")
        buf.write("\u0140\7\20\2\2\u013e\u0140\5\66\34\2\u013f\u013a\3\2")
        buf.write("\2\2\u013f\u013b\3\2\2\2\u013f\u013c\3\2\2\2\u013f\u013d")
        buf.write("\3\2\2\2\u013f\u013e\3\2\2\2\u0140\65\3\2\2\2\u0141\u0142")
        buf.write("\7/\2\2\u0142\u0143\7:\2\2\u0143\u0144\7\60\2\2\u0144")
        buf.write("\u0145\58\35\2\u0145\67\3\2\2\2\u0146\u0147\t\b\2\2\u0147")
        buf.write("9\3\2\2\2\36=CPUZcw}\u0086\u008c\u0095\u009d\u00ac\u00b1")
        buf.write("\u00b8\u00c1\u00d9\u00e0\u00e2\u00ea\u00f6\u0101\u0107")
        buf.write("\u0119\u0127\u012f\u0135\u013f")
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
                      "RP", "SEMI", "COLON", "LIT", "LIT_EXCEPT_ARRAY", 
                      "FLOAT_LIT", "INT_LIT", "BOOL_LIT", "STRING_LIT", 
                      "ARRAY_LIT", "ID", "AT_ID", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_dcl = 1
    RULE_class_super = 2
    RULE_class_body = 3
    RULE_class_member = 4
    RULE_attribute = 5
    RULE_attribute_inner_without_init = 6
    RULE_attribute_inner_with_init = 7
    RULE_attribute_inner_with_init_tail = 8
    RULE_constructor_method = 9
    RULE_method = 10
    RULE_param_list = 11
    RULE_param = 12
    RULE_expr = 13
    RULE_expr_list = 14
    RULE_stmt = 15
    RULE_dcl_stmt = 16
    RULE_assign_stmt = 17
    RULE_if_stmt = 18
    RULE_for_stmt = 19
    RULE_break_stmt = 20
    RULE_continue_stmt = 21
    RULE_return_stmt = 22
    RULE_method_invocation_stmt = 23
    RULE_block_stmt = 24
    RULE_data_type = 25
    RULE_array_type = 26
    RULE_element_type = 27

    ruleNames =  [ "program", "class_dcl", "class_super", "class_body", 
                   "class_member", "attribute", "attribute_inner_without_init", 
                   "attribute_inner_with_init", "attribute_inner_with_init_tail", 
                   "constructor_method", "method", "param_list", "param", 
                   "expr", "expr_list", "stmt", "dcl_stmt", "assign_stmt", 
                   "if_stmt", "for_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "method_invocation_stmt", "block_stmt", 
                   "data_type", "array_type", "element_type" ]

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
    LIT=53
    LIT_EXCEPT_ARRAY=54
    FLOAT_LIT=55
    INT_LIT=56
    BOOL_LIT=57
    STRING_LIT=58
    ARRAY_LIT=59
    ID=60
    AT_ID=61
    WS=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64
    ERROR_CHAR=65

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
            self.state = 57 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 56
                self.class_dcl()
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSlangParser.CLASS):
                    break

            self.state = 61
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
            self.state = 63
            self.match(CSlangParser.CLASS)
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 64
                self.class_super()


            self.state = 67
            self.match(CSlangParser.ID)
            self.state = 68
            self.match(CSlangParser.LP)
            self.state = 69
            self.class_body()
            self.state = 70
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
            self.state = 72
            self.match(CSlangParser.ID)
            self.state = 73
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
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.VAR) | (1 << CSlangParser.CONST) | (1 << CSlangParser.FUNC))) != 0):
                self.state = 75
                self.class_member()
                self.state = 80
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




    def class_member(self):

        localctx = CSlangParser.Class_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_member)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.attribute()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
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

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def attribute_inner_with_init(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_inner_with_initContext,0)


        def attribute_inner_without_init(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_inner_without_initContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attribute




    def attribute(self):

        localctx = CSlangParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 86
                self.attribute_inner_with_init()
                pass

            elif la_ == 2:
                self.state = 87
                self.attribute_inner_without_init()
                pass


            self.state = 90
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_inner_without_initContext(ParserRuleContext):
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
            return CSlangParser.RULE_attribute_inner_without_init




    def attribute_inner_without_init(self):

        localctx = CSlangParser.Attribute_inner_without_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute_inner_without_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 93
                self.match(CSlangParser.CM)
                self.state = 94
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
            self.match(CSlangParser.COLON)
            self.state = 101
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_inner_with_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_inner_with_init_tail(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_inner_with_init_tailContext,0)


        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attribute_inner_with_init




    def attribute_inner_with_init(self):

        localctx = CSlangParser.Attribute_inner_with_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attribute_inner_with_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 104
            self.attribute_inner_with_init_tail()
            self.state = 105
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_inner_with_init_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def attribute_inner_with_init_tail(self):
            return self.getTypedRuleContext(CSlangParser.Attribute_inner_with_init_tailContext,0)


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
            return CSlangParser.RULE_attribute_inner_with_init_tail




    def attribute_inner_with_init_tail(self):

        localctx = CSlangParser.Attribute_inner_with_init_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attribute_inner_with_init_tail)
        self._la = 0 # Token type
        try:
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.match(CSlangParser.CM)
                self.state = 108
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 109
                self.attribute_inner_with_init_tail()
                self.state = 110
                self.expr(0)
                self.state = 111
                self.match(CSlangParser.CM)
                pass
            elif token in [CSlangParser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(CSlangParser.COLON)
                self.state = 114
                self.data_type()
                self.state = 115
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
        self.enterRule(localctx, 18, self.RULE_constructor_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(CSlangParser.FUNC)
            self.state = 120
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 121
            self.match(CSlangParser.LB)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 122
                self.param_list()


            self.state = 125
            self.match(CSlangParser.RB)
            self.state = 126
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
        self.enterRule(localctx, 20, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(CSlangParser.FUNC)
            self.state = 129
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.AT_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 130
            self.match(CSlangParser.LB)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 131
                self.param_list()


            self.state = 134
            self.match(CSlangParser.RB)
            self.state = 135
            self.match(CSlangParser.COLON)
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.LS]:
                self.state = 136
                self.data_type()
                pass
            elif token in [CSlangParser.VOID]:
                self.state = 137
                self.match(CSlangParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 140
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
        self.enterRule(localctx, 22, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.param()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 143
                self.match(CSlangParser.CM)
                self.state = 144
                self.param()
                self.state = 149
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
        self.enterRule(localctx, 24, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(CSlangParser.ID)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 151
                self.match(CSlangParser.CM)
                self.state = 152
                self.match(CSlangParser.ID)
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 158
            self.match(CSlangParser.COLON)
            self.state = 159
            self.data_type()
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

        def LIT(self):
            return self.getToken(CSlangParser.LIT, 0)

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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 162
                self.match(CSlangParser.LB)
                self.state = 163
                self.expr(0)
                self.state = 164
                self.match(CSlangParser.RB)
                pass

            elif la_ == 2:
                self.state = 166
                self.match(CSlangParser.NEW)
                self.state = 167
                self.match(CSlangParser.ID)
                self.state = 168
                self.match(CSlangParser.LB)
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NEGATE) | (1 << CSlangParser.LB) | (1 << CSlangParser.LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                    self.state = 169
                    self.expr_list()


                self.state = 172
                self.match(CSlangParser.RB)
                pass

            elif la_ == 3:
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 173
                    self.match(CSlangParser.ID)
                    self.state = 174
                    self.match(CSlangParser.DOT)


                self.state = 177
                self.match(CSlangParser.AT_ID)
                self.state = 182
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 178
                    self.match(CSlangParser.LB)
                    self.state = 179
                    self.expr_list()
                    self.state = 180
                    self.match(CSlangParser.RB)


                pass

            elif la_ == 4:
                self.state = 184
                self.match(CSlangParser.SUB_OP)
                self.state = 185
                self.expr(10)
                pass

            elif la_ == 5:
                self.state = 186
                self.match(CSlangParser.NEGATE)
                self.state = 187
                self.expr(9)
                pass

            elif la_ == 6:
                self.state = 188
                self.match(CSlangParser.LIT)
                pass

            elif la_ == 7:
                self.state = 189
                self.match(CSlangParser.SELF)
                pass

            elif la_ == 8:
                self.state = 190
                self.match(CSlangParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 224
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 222
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 193
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 194
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MUL_OP) | (1 << CSlangParser.DIV_OP) | (1 << CSlangParser.BACKSLASH) | (1 << CSlangParser.MOD_OP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 195
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 196
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 197
                        _la = self._input.LA(1)
                        if not(_la==CSlangParser.ADD_OP or _la==CSlangParser.SUB_OP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 198
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = CSlangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 199
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 200
                        _la = self._input.LA(1)
                        if not(_la==CSlangParser.AND or _la==CSlangParser.OR):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 201
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = CSlangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 202
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 203
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.NOT_EQUAL) | (1 << CSlangParser.EQUAL) | (1 << CSlangParser.LESS_EQUAL) | (1 << CSlangParser.LESS_THAN) | (1 << CSlangParser.GREATER_EQUAL) | (1 << CSlangParser.GREATER_THAN))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 204
                        self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = CSlangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 205
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 206
                        self.match(CSlangParser.POW_OP)
                        self.state = 207
                        self.expr(5)
                        pass

                    elif la_ == 6:
                        localctx = CSlangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 208
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 209
                        self.match(CSlangParser.DOT)
                        self.state = 210
                        self.match(CSlangParser.ID)
                        self.state = 215
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                        if la_ == 1:
                            self.state = 211
                            self.match(CSlangParser.LB)
                            self.state = 212
                            self.expr_list()
                            self.state = 213
                            self.match(CSlangParser.RB)


                        pass

                    elif la_ == 7:
                        localctx = CSlangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 217
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 218
                        self.match(CSlangParser.LS)
                        self.state = 219
                        self.expr(0)
                        self.state = 220
                        self.match(CSlangParser.RS)
                        pass

             
                self.state = 226
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        self.enterRule(localctx, 28, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.expr(0)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 228
                self.match(CSlangParser.CM)
                self.state = 229
                self.expr(0)
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stmt)
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.dcl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 238
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 239
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 240
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 241
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 242
                self.method_invocation_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 243
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

        def attribute(self):
            return self.getTypedRuleContext(CSlangParser.AttributeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_dcl_stmt




    def dcl_stmt(self):

        localctx = CSlangParser.Dcl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_dcl_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.attribute()
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




    def assign_stmt(self):

        localctx = CSlangParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.expr(0)
            self.state = 249
            self.match(CSlangParser.DECLARE_ASSIGN_OP)
            self.state = 250
            self.expr(0)
            self.state = 251
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
        self.enterRule(localctx, 36, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(CSlangParser.IF)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LP:
                self.state = 254
                self.block_stmt()


            self.state = 257
            self.expr(0)
            self.state = 258
            self.block_stmt()
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 259
                self.match(CSlangParser.ELSE)
                self.state = 260
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




    def for_stmt(self):

        localctx = CSlangParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(CSlangParser.FOR)
            self.state = 264
            self.assign_stmt()
            self.state = 265
            self.match(CSlangParser.SEMI)
            self.state = 266
            self.expr(0)
            self.state = 267
            self.match(CSlangParser.SEMI)
            self.state = 268
            self.assign_stmt()
            self.state = 269
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
        self.enterRule(localctx, 40, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(CSlangParser.BREAK)
            self.state = 272
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
        self.enterRule(localctx, 42, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(CSlangParser.CONTINUE)
            self.state = 275
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
        self.enterRule(localctx, 44, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(CSlangParser.RETURN)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NEGATE) | (1 << CSlangParser.LB) | (1 << CSlangParser.LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 278
                self.expr(0)


            self.state = 281
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

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(CSlangParser.Expr_listContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_method_invocation_stmt




    def method_invocation_stmt(self):

        localctx = CSlangParser.Method_invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_method_invocation_stmt)
        self._la = 0 # Token type
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.expr(0)
                self.state = 284
                self.match(CSlangParser.DOT)
                self.state = 285
                self.match(CSlangParser.ID)
                self.state = 286
                self.match(CSlangParser.LB)
                self.state = 287
                self.expr_list()
                self.state = 288
                self.match(CSlangParser.RB)
                self.state = 289
                self.match(CSlangParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 291
                    self.match(CSlangParser.ID)
                    self.state = 292
                    self.match(CSlangParser.DOT)


                self.state = 295
                self.match(CSlangParser.AT_ID)
                self.state = 296
                self.match(CSlangParser.LB)
                self.state = 297
                self.expr_list()
                self.state = 298
                self.match(CSlangParser.RB)
                self.state = 299
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




    def block_stmt(self):

        localctx = CSlangParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(CSlangParser.LP)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.VAR) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.CONST) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NEGATE) | (1 << CSlangParser.LB) | (1 << CSlangParser.LP) | (1 << CSlangParser.LIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.AT_ID))) != 0):
                self.state = 304
                self.stmt()
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 310
            self.match(CSlangParser.RP)
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




    def data_type(self):

        localctx = CSlangParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_data_type)
        try:
            self.state = 317
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.BOOL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.match(CSlangParser.BOOL)
                pass
            elif token in [CSlangParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.match(CSlangParser.INT)
                pass
            elif token in [CSlangParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 314
                self.match(CSlangParser.FLOAT)
                pass
            elif token in [CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 315
                self.match(CSlangParser.STRING)
                pass
            elif token in [CSlangParser.LS]:
                self.enterOuterAlt(localctx, 5)
                self.state = 316
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




    def array_type(self):

        localctx = CSlangParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(CSlangParser.LS)
            self.state = 320
            self.match(CSlangParser.INT_LIT)
            self.state = 321
            self.match(CSlangParser.RS)
            self.state = 322
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




    def element_type(self):

        localctx = CSlangParser.Element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_element_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
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
        self._predicates[13] = self.expr_sempred
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
         




