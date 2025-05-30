ARCH = {
  "mach": "EM_AARCH64",
  "endianness": "little",
  "bits": 64,
  "instr_bytes": 4,
  "rel": "rela",
  "pltsz": 16,
  "reloc_prefix": "R_AARCH64",
  "relocs": [
    # Null relocation: also 0x100 for ELF64
    "NONE",
    # Data relocations
    "ABS64",
    "ABS32",
    "ABS16",
    "PREL64",
    "PREL32",
    "PREL16",
    # Static AArch64 relocations
    "MOVW_UABS_G0",
    "MOVW_UABS_G0_NC",
    "MOVW_UABS_G1",
    "MOVW_UABS_G1_NC",
    "MOVW_UABS_G2",
    "MOVW_UABS_G2_NC",
    "MOVW_UABS_G3",
    "MOVW_SABS_G0",
    "MOVW_SABS_G1",
    "MOVW_SABS_G2",
    "LD_PREL_LO19",
    "ADR_PREL_LO21",
    "ADR_PREL_PG_HI21",
    "ADR_PREL_PG_HI21_NC",
    "ADD_ABS_LO12_NC",
    "LDST8_ABS_LO12_NC",
    "TSTBR14",
    "CONDBR19",
    "JUMP26",
    "CALL26",
    "LDST16_ABS_LO12_NC",
    "LDST32_ABS_LO12_NC",
    "LDST64_ABS_LO12_NC",
    "MOVW_PREL_G0",
    "MOVW_PREL_G0_NC",
    "MOVW_PREL_G1",
    "MOVW_PREL_G1_NC",
    "MOVW_PREL_G2",
    "MOVW_PREL_G2_NC",
    "MOVW_PREL_G3",
    "LDST128_ABS_LO12_NC",
    "MOVW_GOTOFF_G0",
    "MOVW_GOTOFF_G0_NC",
    "MOVW_GOTOFF_G1",
    "MOVW_GOTOFF_G1_NC",
    "MOVW_GOTOFF_G2",
    "MOVW_GOTOFF_G2_NC",
    "MOVW_GOTOFF_G3",
    "GOTREL64",
    "GOTREL32",
    "GOT_LD_PREL19",
    "LD64_GOTOFF_LO15",
    "ADR_GOT_PAGE",
    "LD64_GOT_LO12_NC",
    "LD64_GOTPAGE_LO15",
    "PLT32",
    "GOTPCREL32",
    # General dynamic TLS relocations
    "TLSGD_ADR_PREL21",
    "TLSGD_ADR_PAGE21",
    "TLSGD_ADD_LO12_NC",
    "TLSGD_MOVW_G1",
    "TLSGD_MOVW_G0_NC",
    # Local dynamic TLS relocations
    "TLSLD_ADR_PREL21",
    "TLSLD_ADR_PAGE21",
    "TLSLD_ADD_LO12_NC",
    "TLSLD_MOVW_G1",
    "TLSLD_MOVW_G0_NC",
    "TLSLD_LD_PREL19",
    "TLSLD_MOVW_DTPREL_G2",
    "TLSLD_MOVW_DTPREL_G1",
    "TLSLD_MOVW_DTPREL_G1_NC",
    "TLSLD_MOVW_DTPREL_G0",
    "TLSLD_MOVW_DTPREL_G0_NC",
    "TLSLD_ADD_DTPREL_HI12",
    "TLSLD_ADD_DTPREL_LO12",
    "TLSLD_ADD_DTPREL_LO12_NC",
    "TLSLD_LDST8_DTPREL_LO12",
    "TLSLD_LDST8_DTPREL_LO12_NC",
    "TLSLD_LDST16_DTPREL_LO12",
    "TLSLD_LDST16_DTPREL_LO12_NC",
    "TLSLD_LDST32_DTPREL_LO12",
    "TLSLD_LDST32_DTPREL_LO12_NC",
    "TLSLD_LDST64_DTPREL_LO12",
    "TLSLD_LDST64_DTPREL_LO12_NC",
    "TLSIE_MOVW_GOTTPREL_G1",
    "TLSIE_MOVW_GOTTPREL_G0_NC",
    "TLSIE_ADR_GOTTPREL_PAGE21",
    "TLSIE_LD64_GOTTPREL_LO12_NC",
    "TLSIE_LD_GOTTPREL_PREL19",
    # Local exec TLS relocations
    "TLSLE_MOVW_TPREL_G2",
    "TLSLE_MOVW_TPREL_G1",
    "TLSLE_MOVW_TPREL_G1_NC",
    "TLSLE_MOVW_TPREL_G0",
    "TLSLE_MOVW_TPREL_G0_NC",
    "TLSLE_ADD_TPREL_HI12",
    "TLSLE_ADD_TPREL_LO12",
    "TLSLE_ADD_TPREL_LO12_NC",
    "TLSLE_LDST8_TPREL_LO12",
    "TLSLE_LDST8_TPREL_LO12_NC",
    "TLSLE_LDST16_TPREL_LO12",
    "TLSLE_LDST16_TPREL_LO12_NC",
    "TLSLE_LDST32_TPREL_LO12",
    "TLSLE_LDST32_TPREL_LO12_NC",
    "TLSLE_LDST64_TPREL_LO12",
    "TLSLE_LDST64_TPREL_LO12_NC",
    # TLS descriptor relocations
    "TLSDESC_LD_PREL19",
    "TLSDESC_ADR_PREL21",
    "TLSDESC_ADR_PAGE21",
    "TLSDESC_LD64_LO12",
    "TLSDESC_ADD_LO12",
    "TLSDESC_OFF_G1",
    "TLSDESC_OFF_G0_NC",
    "TLSDESC_LDR",
    "TLSDESC_ADD",
    "TLSDESC_CALL",
    "TLSLE_LDST128_TPREL_LO12",
    "TLSLE_LDST128_TPREL_LO12_NC",
    "TLSLD_LDST128_DTPREL_LO12",
    "TLSLD_LDST128_DTPREL_LO12_NC",
    # Dynamic relocations
    "COPY",
    "GLOB_DAT",
    "JUMP_SLOT",
    "RELATIVE",
    # 0x404 and 0x405 are now R_AARCH64_TLS_IMPDEF1 and _TLS_IMPDEF2
    # We follow GNU and define TLS_IMPDEF1 as TLS_DTPMODS_IMPDEF2 as
    # TLS_DTPREL64
    "TLS_DTPMOD64",
    "TLS_DTPREL64",
    "TLS_TPREL64",
    "TLSDESC",
    "IRELATIVE",
    # PAuthABI static and dynamic relocations: defined iielf64,
    # https://github.com/ARM-software/abi-aa
    "AUTH_ABS64",
    "AUTH_RELATIVE",
    # ELF32
    # # R_AARCH64_P32_NONE",
    # "P32_ABS32",
    # "P32_ABS16",
    # "P32_PREL32",
    # "P32_PREL16",
    # "P32_MOVW_UABS_G0",
    # "P32_MOVW_UABS_G0_NC",
    # "P32_MOVW_UABS_G1",
    # "P32_MOVW_SABS_G0",
    # "P32_LD_PREL_LO19",
    # "P32_ADR_PREL_LO21",
    # "P32_ADR_PREL_PG_HI21",
    # "P32_ADD_ABS_LO12_NC",
    # "P32_LDST8_ABS_LO12_NC",
    # "P32_LDST16_ABS_LO12_NC",
    # "P32_LDST32_ABS_LO12_NC",
    # "P32_LDST64_ABS_LO12_NC",
    # "P32_LDST128_ABS_LO12_NC",
    # "P32_TSTBR14",
    # "P32_CONDBR19",
    # "P32_JUMP26",
    # "P32_CALL26",
    # "P32_MOVW_PREL_G0",
    # "P32_MOVW_PREL_G0_NC",
    # "P32_MOVW_PREL_G1",
    # "P32_GOT_LD_PREL19",
    # "P32_ADR_GOT_PAGE",
    # "P32_LD32_GOT_LO12_NC",
    # "P32_LD32_GOTPAGE_LO14",
    # "P32_PLT32",
    # "P32_TLSGD_ADR_PREL21",
    # "P32_TLSGD_ADR_PAGE21",
    # "P32_TLSGD_ADD_LO12_NC",
    # "P32_TLSLD_ADR_PREL21",
    # "P32_TLSLD_ADR_PAGE21",
    # "P32_TLSLD_ADD_LO12_NC",
    # "P32_TLSLD_LD_PREL19",
    # "P32_TLSLD_MOVW_DTPREL_G1",
    # "P32_TLSLD_MOVW_DTPREL_G0",
    # "P32_TLSLD_MOVW_DTPREL_G0_NC",
    # "P32_TLSLD_ADD_DTPREL_HI12",
    # "P32_TLSLD_ADD_DTPREL_LO12",
    # "P32_TLSLD_ADD_DTPREL_LO12_NC",
    # "P32_TLSLD_LDST8_DTPREL_LO12",
    # "P32_TLSLD_LDST8_DTPREL_LO12_NC",
    # "P32_TLSLD_LDST16_DTPREL_LO12",
    # "P32_TLSLD_LDST16_DTPREL_LO12_NC",
    # "P32_TLSLD_LDST32_DTPREL_LO12",
    # "P32_TLSLD_LDST32_DTPREL_LO12_NC",
    # "P32_TLSLD_LDST64_DTPREL_LO12",
    # "P32_TLSLD_LDST64_DTPREL_LO12_NC",
    # "P32_TLSLD_LDST128_DTPREL_LO12",
    # "P32_TLSLD_LDST128_DTPREL_LO12_NC,
    # "P32_TLSIE_ADR_GOTTPREL_PAGE21",
    # "P32_TLSIE_LD32_GOTTPREL_LO12_NC",
    # "P32_TLSIE_LD_GOTTPREL_PREL19",
    # "P32_TLSLE_MOVW_TPREL_G1",
    # "P32_TLSLE_MOVW_TPREL_G0",
    # "P32_TLSLE_MOVW_TPREL_G0_NC",
    # "P32_TLSLE_ADD_TPREL_HI12",
    # "P32_TLSLE_ADD_TPREL_LO12",
    # "P32_TLSLE_ADD_TPREL_LO12_NC",
    # "P32_TLSLE_LDST8_TPREL_LO12",
    # "P32_TLSLE_LDST8_TPREL_LO12_NC",
    # "P32_TLSLE_LDST16_TPREL_LO12",
    # "P32_TLSLE_LDST16_TPREL_LO12_NC",
    # "P32_TLSLE_LDST32_TPREL_LO12",
    # "P32_TLSLE_LDST32_TPREL_LO12_NC",
    # "P32_TLSLE_LDST64_TPREL_LO12",
    # "P32_TLSLE_LDST64_TPREL_LO12_NC",
    # "P32_TLSLE_LDST128_TPREL_LO12",
    # "P32_TLSLE_LDST128_TPREL_LO12_NC",
    # "P32_TLSDESC_LD_PREL19",
    # "P32_TLSDESC_ADR_PREL21",
    # "P32_TLSDESC_ADR_PAGE21",
    # "P32_TLSDESC_LD32_LO12",
    # "P32_TLSDESC_ADD_LO12",
    # "P32_TLSDESC_CALL",
    # # Dynamic relocations
    # "P32_COPY",
    # "P32_GLOB_DAT",
    # "P32_JUMP_SLOT",
    # "P32_RELATIVE",
    # "P32_TLS_DTPREL",
    # "P32_TLS_DTPMOD",
    # "P32_TLS_TPREL",
    # "P32_TLSDESC",
    # "P32_IRELATIVE",
  ],
  "dyn_relocs": {
    257: "ABS64",
    1024 + 0: "COPY",
    1024 + 1: "GLOB_DAT",
    1024 + 2: "JUMP_SLOT",
    1024 + 3: "RELATIVE",
    1024 + 4: "TLS_DTPMOD64",
    1024 + 5: "TLS_DTPREL64",
    1024 + 6: "TLS_TPREL64",
    1024 + 7: "TLSDESC",
    1024 + 8: "IRELATIVE",
  },
}
