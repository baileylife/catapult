# Copyright (c) 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'tracing_css_files': [
      'trace_viewer/extras/about_tracing/common.css',
      'trace_viewer/extras/chrome/cc/display_item_view.css',
      'trace_viewer/extras/chrome/cc/layer_picker.css',
      'trace_viewer/extras/chrome/cc/layer_tree_host_impl_view.css',
      'trace_viewer/extras/chrome/cc/layer_view.css',
      'trace_viewer/extras/chrome/cc/picture_ops_chart_summary_view.css',
      'trace_viewer/extras/chrome/cc/picture_ops_chart_view.css',
      'trace_viewer/extras/chrome/cc/picture_ops_list_view.css',
      'trace_viewer/extras/chrome/cc/picture_view.css',
      'trace_viewer/extras/chrome/gpu/state_view.css',
      'trace_viewer/extras/system_stats/system_stats_instance_track.css',
      'trace_viewer/extras/system_stats/system_stats_snapshot_view.css',
      'trace_viewer/extras/tcmalloc/heap_instance_track.css',
      'trace_viewer/extras/tcmalloc/tcmalloc_instance_view.css',
      'trace_viewer/extras/tcmalloc/tcmalloc_snapshot_view.css',
      'trace_viewer/ui/analysis/analysis_results.css',
      'trace_viewer/ui/base/common.css',
      'trace_viewer/ui/base/drag_handle.css',
      'trace_viewer/ui/base/line_chart.css',
      'trace_viewer/ui/base/list_view.css',
      'trace_viewer/ui/base/mouse_mode_selector.css',
      'trace_viewer/ui/base/pie_chart.css',
      'trace_viewer/ui/base/sortable_table.css',
      'trace_viewer/ui/base/sunburst_chart.css',
      'trace_viewer/ui/base/tool_button.css',
      'trace_viewer/ui/timeline_track_view.css',
      'trace_viewer/ui/timeline_view.css',
      'trace_viewer/ui/tracks/drawing_container.css',
      'trace_viewer/ui/tracks/heading_track.css',
      'trace_viewer/ui/tracks/object_instance_track.css',
      'trace_viewer/ui/tracks/process_track_base.css',
      'trace_viewer/ui/tracks/rect_track.css',
      'trace_viewer/ui/tracks/ruler_track.css',
      'trace_viewer/ui/tracks/spacing_track.css',
      'trace_viewer/ui/tracks/thread_track.css',
      'trace_viewer/ui/tracks/track.css',
    ],
    'tracing_js_html_files': [
      'trace_viewer/base/base.html',
      'trace_viewer/base/base64.html',
      'trace_viewer/base/bbox2.html',
      'trace_viewer/base/category_util.html',
      'trace_viewer/base/color.html',
      'trace_viewer/base/deep_utils.html',
      'trace_viewer/base/event_target.html',
      'trace_viewer/base/events.html',
      'trace_viewer/base/extension_registry.html',
      'trace_viewer/base/extension_registry_base.html',
      'trace_viewer/base/extension_registry_basic.html',
      'trace_viewer/base/extension_registry_type_based.html',
      'trace_viewer/base/guid.html',
      'trace_viewer/base/interval_tree.html',
      'trace_viewer/base/iteration_helpers.html',
      'trace_viewer/base/math.html',
      'trace_viewer/base/properties.html',
      'trace_viewer/base/quad.html',
      'trace_viewer/base/range.html',
      'trace_viewer/base/range_utils.html',
      'trace_viewer/base/rect.html',
      'trace_viewer/base/settings.html',
      'trace_viewer/base/sorted_array_utils.html',
      'trace_viewer/base/statistics.html',
      'trace_viewer/base/task.html',
      'trace_viewer/base/units/size_in_bytes.html',
      'trace_viewer/base/units/time.html',
      'trace_viewer/base/units/time_duration.html',
      'trace_viewer/base/units/time_stamp.html',
      'trace_viewer/base/units/util.html',
      'trace_viewer/base/utils.html',
      'trace_viewer/core/auditor.html',
      'trace_viewer/core/brushing_state.html',
      'trace_viewer/core/constants.html',
      'trace_viewer/core/event_presenter.html',
      'trace_viewer/core/fast_rect_renderer.html',
      'trace_viewer/core/favicons.html',
      'trace_viewer/core/filter.html',
      'trace_viewer/core/find_control.html',
      'trace_viewer/core/find_controller.html',
      'trace_viewer/core/location.html',
      'trace_viewer/core/scripting_control.html',
      'trace_viewer/core/scripting_controller.html',
      'trace_viewer/core/scripting_object.html',
      'trace_viewer/core/selection.html',
      'trace_viewer/core/selection_controller.html',
      'trace_viewer/core/timing_tool.html',
      'trace_viewer/extras/about_tracing/about_tracing.html',
      'trace_viewer/extras/about_tracing/inspector_connection.html',
      'trace_viewer/extras/about_tracing/inspector_tracing_controller_client.html',
      'trace_viewer/extras/about_tracing/profiling_view.html',
      'trace_viewer/extras/about_tracing/record_and_capture_controller.html',
      'trace_viewer/extras/about_tracing/record_selection_dialog.html',
      'trace_viewer/extras/about_tracing/tracing_controller_client.html',
      'trace_viewer/extras/about_tracing/xhr_based_tracing_controller_client.html',
      'trace_viewer/extras/analysis/sampling_summary.html',
      'trace_viewer/extras/android/android_app.html',
      'trace_viewer/extras/android/android_auditor.html',
      'trace_viewer/extras/android/android_model_helper.html',
      'trace_viewer/extras/android/android_surface_flinger.html',
      'trace_viewer/extras/chrome/cc/cc.html',
      'trace_viewer/extras/chrome/cc/constants.html',
      'trace_viewer/extras/chrome/cc/debug_colors.html',
      'trace_viewer/extras/chrome/cc/display_item_debugger.html',
      'trace_viewer/extras/chrome/cc/display_item_list.html',
      'trace_viewer/extras/chrome/cc/display_item_view.html',
      'trace_viewer/extras/chrome/cc/input_latency_async_slice.html',
      'trace_viewer/extras/chrome/cc/layer_impl.html',
      'trace_viewer/extras/chrome/cc/layer_picker.html',
      'trace_viewer/extras/chrome/cc/layer_tree_host_impl.html',
      'trace_viewer/extras/chrome/cc/layer_tree_host_impl_view.html',
      'trace_viewer/extras/chrome/cc/layer_tree_impl.html',
      'trace_viewer/extras/chrome/cc/layer_tree_quad_stack_view.html',
      'trace_viewer/extras/chrome/cc/layer_view.html',
      'trace_viewer/extras/chrome/cc/picture.html',
      'trace_viewer/extras/chrome/cc/picture_as_image_data.html',
      'trace_viewer/extras/chrome/cc/picture_debugger.html',
      'trace_viewer/extras/chrome/cc/picture_ops_chart_summary_view.html',
      'trace_viewer/extras/chrome/cc/picture_ops_chart_view.html',
      'trace_viewer/extras/chrome/cc/picture_ops_list_view.html',
      'trace_viewer/extras/chrome/cc/picture_view.html',
      'trace_viewer/extras/chrome/cc/raster_task.html',
      'trace_viewer/extras/chrome/cc/raster_task_selection.html',
      'trace_viewer/extras/chrome/cc/raster_task_view.html',
      'trace_viewer/extras/chrome/cc/region.html',
      'trace_viewer/extras/chrome/cc/render_pass.html',
      'trace_viewer/extras/chrome/cc/selection.html',
      'trace_viewer/extras/chrome/cc/tile.html',
      'trace_viewer/extras/chrome/cc/tile_coverage_rect.html',
      'trace_viewer/extras/chrome/cc/tile_view.html',
      'trace_viewer/extras/chrome/cc/util.html',
      'trace_viewer/extras/chrome/chrome_auditor.html',
      'trace_viewer/extras/chrome/chrome_browser_helper.html',
      'trace_viewer/extras/chrome/chrome_model_helper.html',
      'trace_viewer/extras/chrome/chrome_process_helper.html',
      'trace_viewer/extras/chrome/chrome_renderer_helper.html',
      'trace_viewer/extras/chrome/gpu/gpu.html',
      'trace_viewer/extras/chrome/gpu/gpu_async_slice.html',
      'trace_viewer/extras/chrome/gpu/state.html',
      'trace_viewer/extras/chrome/gpu/state_view.html',
      'trace_viewer/extras/chrome/layout_object.html',
      'trace_viewer/extras/chrome_config.html',
      'trace_viewer/extras/full_config.html',
      'trace_viewer/extras/highlighter/vsync_highlighter.html',
      'trace_viewer/extras/importer/battor_importer.html',
      'trace_viewer/extras/importer/ddms_importer.html',
      'trace_viewer/extras/importer/etw/etw_importer.html',
      'trace_viewer/extras/importer/etw/eventtrace_parser.html',
      'trace_viewer/extras/importer/etw/parser.html',
      'trace_viewer/extras/importer/etw/process_parser.html',
      'trace_viewer/extras/importer/etw/thread_parser.html',
      'trace_viewer/extras/importer/gzip_importer.html',
      'trace_viewer/extras/importer/jszip.html',
      'trace_viewer/extras/importer/linux_perf/android_parser.html',
      'trace_viewer/extras/importer/linux_perf/bus_parser.html',
      'trace_viewer/extras/importer/linux_perf/clock_parser.html',
      'trace_viewer/extras/importer/linux_perf/cpufreq_parser.html',
      'trace_viewer/extras/importer/linux_perf/disk_parser.html',
      'trace_viewer/extras/importer/linux_perf/drm_parser.html',
      'trace_viewer/extras/importer/linux_perf/exynos_parser.html',
      'trace_viewer/extras/importer/linux_perf/ftrace_importer.html',
      'trace_viewer/extras/importer/linux_perf/gesture_parser.html',
      'trace_viewer/extras/importer/linux_perf/i915_parser.html',
      'trace_viewer/extras/importer/linux_perf/irq_parser.html',
      'trace_viewer/extras/importer/linux_perf/kfunc_parser.html',
      'trace_viewer/extras/importer/linux_perf/mali_parser.html',
      'trace_viewer/extras/importer/linux_perf/memreclaim_parser.html',
      'trace_viewer/extras/importer/linux_perf/parser.html',
      'trace_viewer/extras/importer/linux_perf/power_parser.html',
      'trace_viewer/extras/importer/linux_perf/regulator_parser.html',
      'trace_viewer/extras/importer/linux_perf/sched_parser.html',
      'trace_viewer/extras/importer/linux_perf/sync_parser.html',
      'trace_viewer/extras/importer/linux_perf/workqueue_parser.html',
      'trace_viewer/extras/importer/trace2html_importer.html',
      'trace_viewer/extras/importer/trace_event_importer.html',
      'trace_viewer/extras/importer/v8/codemap.html',
      'trace_viewer/extras/importer/v8/log_reader.html',
      'trace_viewer/extras/importer/v8/splaytree.html',
      'trace_viewer/extras/importer/v8/v8_log_importer.html',
      'trace_viewer/extras/importer/zip_importer.html',
      'trace_viewer/extras/lean_config.html',
      'trace_viewer/extras/net/net.html',
      'trace_viewer/extras/net/net_async_slice.html',
      'trace_viewer/extras/rail/animation_interaction_record.html',
      'trace_viewer/extras/rail/idle_interaction_record.html',
      'trace_viewer/extras/rail/load_interaction_record.html',
      'trace_viewer/extras/rail/rail_interaction_record.html',
      'trace_viewer/extras/rail/rail_ir_finder.html',
      'trace_viewer/extras/rail/rail_score.html',
      'trace_viewer/extras/rail/rail_score_side_panel.html',
      'trace_viewer/extras/rail/rail_score_span.html',
      'trace_viewer/extras/rail/response_interaction_record.html',
      'trace_viewer/extras/side_panel/alerts_side_panel.html',
      'trace_viewer/extras/side_panel/input_latency_side_panel.html',
      'trace_viewer/extras/side_panel/time_summary_side_panel.html',
      'trace_viewer/extras/system_stats/system_stats.html',
      'trace_viewer/extras/system_stats/system_stats_instance_track.html',
      'trace_viewer/extras/system_stats/system_stats_snapshot.html',
      'trace_viewer/extras/system_stats/system_stats_snapshot_view.html',
      'trace_viewer/extras/systrace_config.html',
      'trace_viewer/extras/tcmalloc/heap.html',
      'trace_viewer/extras/tcmalloc/heap_instance_track.html',
      'trace_viewer/extras/tcmalloc/tcmalloc.html',
      'trace_viewer/extras/tcmalloc/tcmalloc_instance_view.html',
      'trace_viewer/extras/tcmalloc/tcmalloc_snapshot_view.html',
      'trace_viewer/extras/tquery/context.html',
      'trace_viewer/extras/tquery/filter.html',
      'trace_viewer/extras/tquery/filter_all_of.html',
      'trace_viewer/extras/tquery/filter_any_of.html',
      'trace_viewer/extras/tquery/filter_has_ancestor.html',
      'trace_viewer/extras/tquery/filter_has_duration.html',
      'trace_viewer/extras/tquery/filter_has_title.html',
      'trace_viewer/extras/tquery/filter_is_top_level.html',
      'trace_viewer/extras/tquery/tquery.html',
      'trace_viewer/importer/empty_importer.html',
      'trace_viewer/importer/importer.html',
      'trace_viewer/importer/simple_line_reader.html',
      'trace_viewer/model/alert.html',
      'trace_viewer/model/annotation.html',
      'trace_viewer/model/async_slice.html',
      'trace_viewer/model/async_slice_group.html',
      'trace_viewer/model/attribute.html',
      'trace_viewer/model/comment_box_annotation.html',
      'trace_viewer/model/container_memory_dump.html',
      'trace_viewer/model/counter.html',
      'trace_viewer/model/counter_sample.html',
      'trace_viewer/model/counter_series.html',
      'trace_viewer/model/cpu.html',
      'trace_viewer/model/cpu_slice.html',
      'trace_viewer/model/device.html',
      'trace_viewer/model/event.html',
      'trace_viewer/model/event_container.html',
      'trace_viewer/model/event_info.html',
      'trace_viewer/model/flow_event.html',
      'trace_viewer/model/frame.html',
      'trace_viewer/model/global_memory_dump.html',
      'trace_viewer/model/instant_event.html',
      'trace_viewer/model/interaction_record.html',
      'trace_viewer/model/kernel.html',
      'trace_viewer/model/memory_allocator_dump.html',
      'trace_viewer/model/model.html',
      'trace_viewer/model/model_indices.html',
      'trace_viewer/model/model_settings.html',
      'trace_viewer/model/object_collection.html',
      'trace_viewer/model/object_instance.html',
      'trace_viewer/model/object_snapshot.html',
      'trace_viewer/model/process.html',
      'trace_viewer/model/process_base.html',
      'trace_viewer/model/process_memory_dump.html',
      'trace_viewer/model/proxy_selectable_item.html',
      'trace_viewer/model/rect_annotation.html',
      'trace_viewer/model/sample.html',
      'trace_viewer/model/selectable_item.html',
      'trace_viewer/model/selection_state.html',
      'trace_viewer/model/slice.html',
      'trace_viewer/model/slice_group.html',
      'trace_viewer/model/stack_frame.html',
      'trace_viewer/model/thread.html',
      'trace_viewer/model/thread_slice.html',
      'trace_viewer/model/thread_time_slice.html',
      'trace_viewer/model/time_to_object_instance_map.html',
      'trace_viewer/model/timed_event.html',
      'trace_viewer/model/x_marker_annotation.html',
      'trace_viewer/trace_viewer.html',
      'trace_viewer/ui/analysis/alert_sub_view.html',
      'trace_viewer/ui/analysis/analysis_link.html',
      'trace_viewer/ui/analysis/analysis_results.html',
      'trace_viewer/ui/analysis/analysis_sub_view.html',
      'trace_viewer/ui/analysis/analysis_view.html',
      'trace_viewer/ui/analysis/counter_sample_sub_view.html',
      'trace_viewer/ui/analysis/flow_classifier.html',
      'trace_viewer/ui/analysis/generic_object_view.html',
      'trace_viewer/ui/analysis/memory_dump_allocator_details_pane.html',
      'trace_viewer/ui/analysis/memory_dump_overview_pane.html',
      'trace_viewer/ui/analysis/memory_dump_sub_view_util.html',
      'trace_viewer/ui/analysis/memory_dump_view.html',
      'trace_viewer/ui/analysis/memory_dump_vm_regions_details_pane.html',
      'trace_viewer/ui/analysis/multi_async_slice_sub_view.html',
      'trace_viewer/ui/analysis/multi_cpu_slice_sub_view.html',
      'trace_viewer/ui/analysis/multi_event_details_table.html',
      'trace_viewer/ui/analysis/multi_event_sub_view.html',
      'trace_viewer/ui/analysis/multi_event_summary.html',
      'trace_viewer/ui/analysis/multi_event_summary_table.html',
      'trace_viewer/ui/analysis/multi_flow_event_sub_view.html',
      'trace_viewer/ui/analysis/multi_frame_sub_view.html',
      'trace_viewer/ui/analysis/multi_global_memory_dump_sub_view.html',
      'trace_viewer/ui/analysis/multi_instant_event_sub_view.html',
      'trace_viewer/ui/analysis/multi_interaction_record_sub_view.html',
      'trace_viewer/ui/analysis/multi_object_sub_view.html',
      'trace_viewer/ui/analysis/multi_process_memory_dump_sub_view.html',
      'trace_viewer/ui/analysis/multi_sample_sub_view.html',
      'trace_viewer/ui/analysis/multi_thread_slice_sub_view.html',
      'trace_viewer/ui/analysis/multi_thread_time_slice_sub_view.html',
      'trace_viewer/ui/analysis/object_instance_view.html',
      'trace_viewer/ui/analysis/object_snapshot_view.html',
      'trace_viewer/ui/analysis/related_events.html',
      'trace_viewer/ui/analysis/selection_summary_table.html',
      'trace_viewer/ui/analysis/single_async_slice_sub_view.html',
      'trace_viewer/ui/analysis/single_cpu_slice_sub_view.html',
      'trace_viewer/ui/analysis/single_event_sub_view.html',
      'trace_viewer/ui/analysis/single_flow_event_sub_view.html',
      'trace_viewer/ui/analysis/single_frame_sub_view.html',
      'trace_viewer/ui/analysis/single_global_memory_dump_sub_view.html',
      'trace_viewer/ui/analysis/single_instant_event_sub_view.html',
      'trace_viewer/ui/analysis/single_interaction_record_sub_view.html',
      'trace_viewer/ui/analysis/single_object_instance_sub_view.html',
      'trace_viewer/ui/analysis/single_object_snapshot_sub_view.html',
      'trace_viewer/ui/analysis/single_process_memory_dump_sub_view.html',
      'trace_viewer/ui/analysis/single_sample_sub_view.html',
      'trace_viewer/ui/analysis/single_thread_slice_sub_view.html',
      'trace_viewer/ui/analysis/single_thread_time_slice_sub_view.html',
      'trace_viewer/ui/analysis/stack_frame.html',
      'trace_viewer/ui/analysis/tab_view.html',
      'trace_viewer/ui/annotations/annotation_view.html',
      'trace_viewer/ui/annotations/comment_box_annotation_view.html',
      'trace_viewer/ui/annotations/rect_annotation_view.html',
      'trace_viewer/ui/annotations/x_marker_annotation_view.html',
      'trace_viewer/ui/base/animation.html',
      'trace_viewer/ui/base/animation_controller.html',
      'trace_viewer/ui/base/camera.html',
      'trace_viewer/ui/base/chart_base.html',
      'trace_viewer/ui/base/color_legend.html',
      'trace_viewer/ui/base/color_scheme.html',
      'trace_viewer/ui/base/color_utils.html',
      'trace_viewer/ui/base/container_that_decorates_its_children.html',
      'trace_viewer/ui/base/d3.html',
      'trace_viewer/ui/base/dom_helpers.html',
      'trace_viewer/ui/base/drag_handle.html',
      'trace_viewer/ui/base/draw_helpers.html',
      'trace_viewer/ui/base/dropdown.html',
      'trace_viewer/ui/base/elided_cache.html',
      'trace_viewer/ui/base/info_bar.html',
      'trace_viewer/ui/base/info_bar_group.html',
      'trace_viewer/ui/base/key_event_manager.html',
      'trace_viewer/ui/base/line_chart.html',
      'trace_viewer/ui/base/list_view.html',
      'trace_viewer/ui/base/mouse_mode_selector.html',
      'trace_viewer/ui/base/mouse_tracker.html',
      'trace_viewer/ui/base/overlay.html',
      'trace_viewer/ui/base/pie_chart.html',
      'trace_viewer/ui/base/polymer_utils.html',
      'trace_viewer/ui/base/quad_stack_view.html',
      'trace_viewer/ui/base/raf.html',
      'trace_viewer/ui/base/sortable_table.html',
      'trace_viewer/ui/base/sunburst_chart.html',
      'trace_viewer/ui/base/table.html',
      'trace_viewer/ui/base/toolbar_button.html',
      'trace_viewer/ui/base/ui.html',
      'trace_viewer/ui/base/ui_state.html',
      'trace_viewer/ui/base/utils.html',
      'trace_viewer/ui/side_panel/side_panel.html',
      'trace_viewer/ui/side_panel/side_panel_container.html',
      'trace_viewer/ui/timeline_display_transform.html',
      'trace_viewer/ui/timeline_display_transform_animations.html',
      'trace_viewer/ui/timeline_interest_range.html',
      'trace_viewer/ui/timeline_track_view.html',
      'trace_viewer/ui/timeline_view.html',
      'trace_viewer/ui/timeline_viewport.html',
      'trace_viewer/ui/tracks/alert_track.html',
      'trace_viewer/ui/tracks/async_slice_group_track.html',
      'trace_viewer/ui/tracks/chart_axis.html',
      'trace_viewer/ui/tracks/chart_point.html',
      'trace_viewer/ui/tracks/chart_series.html',
      'trace_viewer/ui/tracks/chart_track.html',
      'trace_viewer/ui/tracks/chart_transform.html',
      'trace_viewer/ui/tracks/container_to_track_map.html',
      'trace_viewer/ui/tracks/container_track.html',
      'trace_viewer/ui/tracks/counter_track.html',
      'trace_viewer/ui/tracks/cpu_track.html',
      'trace_viewer/ui/tracks/drawing_container.html',
      'trace_viewer/ui/tracks/frame_track.html',
      'trace_viewer/ui/tracks/global_memory_dump_track.html',
      'trace_viewer/ui/tracks/heading_track.html',
      'trace_viewer/ui/tracks/highlighter.html',
      'trace_viewer/ui/tracks/kernel_track.html',
      'trace_viewer/ui/tracks/letter_dot_track.html',
      'trace_viewer/ui/tracks/memory_dump_track_util.html',
      'trace_viewer/ui/tracks/model_track.html',
      'trace_viewer/ui/tracks/multi_row_track.html',
      'trace_viewer/ui/tracks/object_instance_group_track.html',
      'trace_viewer/ui/tracks/object_instance_track.html',
      'trace_viewer/ui/tracks/process_memory_dump_track.html',
      'trace_viewer/ui/tracks/process_summary_track.html',
      'trace_viewer/ui/tracks/process_track.html',
      'trace_viewer/ui/tracks/process_track_base.html',
      'trace_viewer/ui/tracks/rect_track.html',
      'trace_viewer/ui/tracks/ruler_track.html',
      'trace_viewer/ui/tracks/sample_track.html',
      'trace_viewer/ui/tracks/slice_group_track.html',
      'trace_viewer/ui/tracks/slice_track.html',
      'trace_viewer/ui/tracks/spacing_track.html',
      'trace_viewer/ui/tracks/stacked_bars_track.html',
      'trace_viewer/ui/tracks/thread_track.html',
      'trace_viewer/ui/tracks/track.html',
      'trace_viewer/ui/units/size_in_bytes_span.html',
      'trace_viewer/ui/units/time_duration_span.html',
      'trace_viewer/ui/units/time_stamp_span.html',
    ],
    'tracing_img_files': [
      'trace_viewer/extras/chrome/cc/images/input-event.png',
      'trace_viewer/extras/chrome/gpu/images/checkerboard.png',
      'trace_viewer/extras/tcmalloc/images/collapse.png',
      'trace_viewer/extras/tcmalloc/images/expand.png',
      'trace_viewer/ui/images/chrome-left.png',
      'trace_viewer/ui/images/chrome-mid.png',
      'trace_viewer/ui/images/chrome-right.png',
      'trace_viewer/ui/images/ui-states.png',
    ],
    'tracing_files': [
      '<@(tracing_css_files)',
      '<@(tracing_js_html_files)',
      '<@(tracing_img_files)',
    ],
  }
}
