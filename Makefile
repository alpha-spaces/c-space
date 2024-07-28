# Copyright 2024 Remy Blank <remy@c-space.org>
# SPDX-License-Identifier: CC-BY-NC-SA-4.0

.PHONY: default
default: download

.PHONY: download
download:
	@cd htdocs; ../tools/gen-index.py download
