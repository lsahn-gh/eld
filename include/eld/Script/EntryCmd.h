//===- EntryCmd.h----------------------------------------------------------===//
// Part of the eld Project, under the BSD License
// See https://github.com/qualcomm/eld/LICENSE.txt for license information.
// SPDX-License-Identifier: BSD-3-Clause
//===----------------------------------------------------------------------===//
//
//                     The MCLinker Project
//
// This file is distributed under the University of Illinois Open Source
// License. See LICENSE.TXT for details.
//
//===----------------------------------------------------------------------===//

#ifndef ELD_SCRIPT_ENTRYCMD_H
#define ELD_SCRIPT_ENTRYCMD_H

#include "eld/Script/ScriptCommand.h"
#include <string>

namespace eld {

class Module;

/** \class EntryCmd
 *  \brief This class defines the interfaces to Entry command.
 */

class EntryCmd : public ScriptCommand {
public:
  EntryCmd(const std::string &PEntry);
  ~EntryCmd();

  void dump(llvm::raw_ostream &Outs) const override;

  static bool classof(const ScriptCommand *LinkerScriptCommand) {
    return LinkerScriptCommand->getKind() == ScriptCommand::ENTRY;
  }

  eld::Expected<void> activate(Module &CurModule) override;

private:
  std::string EntrySymbol;
};

} // namespace eld

#endif
