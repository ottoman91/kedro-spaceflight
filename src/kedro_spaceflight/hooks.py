from typing import Any, Dict, Iterable, Optional

from kedro.framework.hooks import hook_impl
from kedro.pipeline import Pipeline
from kedro.config import ConfigLoader
from kedro.io import DataCatalog
from kedro.versioning import Journal


from kedro_spaceflight.pipelines.data_engineering import pipeline as de
from kedro_spaceflight.pipelines.data_science import pipeline as ds

class ProjectHooks:
    @hook_impl
    def register_pipelines(self) -> Dict[str, Pipeline]:
        """Register the project's pipeline.

        Returns:
            A mapping from a pipeline name to a ``Pipeline`` object.

        """
        de_pipeline = de.create_pipeline()
        ds_pipeline = ds.create_pipeline()

        return {
            "__default__": de_pipeline + ds_pipeline,
            "de": de_pipeline,
            "ds": ds_pipeline,
        }

    @hook_impl
    def register_config_loader(self, conf_paths: Iterable[str]) -> ConfigLoader:
        return ConfigLoader(conf_paths)

    @hook_impl
    def register_catalog(
        self,
        catalog: Optional[Dict[str, Dict[str, Any]]],
        credentials: Dict[str, Dict[str, Any]],
        load_versions: Dict[str, str],
        save_version: str,
        journal: Journal,
    ) -> DataCatalog:
        return DataCatalog.from_config(
            catalog, credentials, load_versions, save_version, journal
        )

#project_hooks = ProjectHooks()
